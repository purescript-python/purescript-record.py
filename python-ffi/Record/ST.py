def copyRecord(rec):
    return {k: v for k, v in rec.items()}


def freeze(rec):
    return lambda: copyRecord(rec)


def thaw(rec):
    return lambda: copyRecord(rec)


def unsafePeek(l):
    def record(rec):
        return lambda: rec[l]

    return record


def unsafePoke(l):
    def key(a):
        def record(rec):
            def ap():
                rec[l] = a

            return ap

        return record

    return key


def unsafeModify(l):
    def modify(f):
        def record(rec):
            def ap():
                rec[l] = f(rec[l])

            return ap

        return record

    return modify
