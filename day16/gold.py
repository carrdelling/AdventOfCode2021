import operator
from functools import reduce


def parse_literal(msg):

    all_bits = []
    while msg:
        chunk, msg = msg[:5], msg[5:]
        ctrl, bits = chunk[0], chunk[1:]

        all_bits.append(bits)

        if ctrl == '0':
            break
    return int(''.join(all_bits), 2), msg


def parse(msg):

    while msg:

        # is this the end?
        if len(set(msg)) < 2:
            return

        vt, msg = msg[:6], msg[6:]
        v, t = vt[:3], vt[3:]

        version = int(v, 2)
        id_type = int(t, 2)

        # just a literal
        if id_type == 4:
            lit, msg = parse_literal(msg)
            packet = (version, id_type, "LIT", lit)
            yield packet
            continue

        # an operator
        l_type, msg = msg[0], msg[1:]

        if l_type == '0':
            tl, msg = msg[:15], msg[15:]
            total_length = int(tl, 2)
            packet = (version, id_type, "OPTYPE 0", total_length)
            yield packet

            subpackets, msg = msg[:total_length], msg[total_length:]

            for packet in parse(subpackets):
                yield packet
            breaker = (0, -1, 'BREAK', '0')
            yield breaker
            continue
        else:
            ns, msg = msg[:11], msg[11:]
            number_subpackets = int(ns, 2)
            packet = (version, id_type, "OPTYPE 1", number_subpackets)
            yield packet
            continue


def calculate(data):

    while data:
        tail = []
        element = data.pop()

        # read until we find an operator
        while element[2] in {'LIT', 'BREAK'}:
            tail.append(element)
            if not data:
                # there was just a literal - go away
                return element[-1]
            element = data.pop()

        _, id_type, msg, v = element
        max_tokens = v if msg == 'OPTYPE 1' else 9E99

        # we need to save the tokens we don't need for later
        tokens = []
        _, _, msg, v = tail.pop()
        while msg != 'BREAK' and len(tokens) < max_tokens:
            tokens.append(v)
            if not tail or len(tokens) >= max_tokens:
                break
            _, _, msg, v = tail.pop()

        # apply the operation
        funcs = {
            0: sum,
            1: operator.mul,
            2: min,
            3: max,
            5: operator.gt,
            6: operator.lt,
            7: operator.eq
        }
        if id_type in {0, 2, 3}:
            result = funcs[id_type](tokens)
        elif id_type in {1, 5, 6, 7}:
            result = reduce(funcs[id_type], tokens)
        else:
            assert False

        # append the result and the rest of the tail (reversed)
        data.append((99, 4, 'LIT', result))
        data += tail[::-1]
        continue



def solve(packet):

    def binarize(text):
        return ''.join(str(int(c, 16) >> (3 - i) & 1) for c in text for i in range(4))

    packets = [p for p in parse(binarize(packet))]
    solution = calculate(packets)

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
