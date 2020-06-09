def copyRecord(rec):
    return {k: v for k, v in rec.items()}

def unsafeInsert(l):
    def value(a):
        def ap(rec):
            rec[l] = a
            return rec

        return ap

    return value


def unsafeModify(l):
    def modify(f):
        def ap(rec):
            rec[l] = f(rec[l])
            return rec

        return ap

    return modify



def unsafeDelete(l):
    def ap(rec):
        del rec[l]
        return rec

    return ap


def unsafeRename(l1):
    def name_to(l2):
        def ap(rec):
            rec[l2] = rec[l1]
            del rec[l1]
            return rec

        return ap

    return name_to
