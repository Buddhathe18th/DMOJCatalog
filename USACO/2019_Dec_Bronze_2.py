f = open("whereami.in", "r")

length = int(f.readline())

mailboxes = f.readline()


def function(length, mailboxes):
    for i in range(1, length + 1):
        substring = [mailboxes[j:j + i] for j in range(0, length - i + 1)]
        unique = set(substring)

        if len(unique) == len(substring):
            return i

    return length


f = open("whereami.out", "w")
f.write(str(function(length, mailboxes)))
f.close()