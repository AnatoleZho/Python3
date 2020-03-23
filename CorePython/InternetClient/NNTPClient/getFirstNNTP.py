
#!/usr/bin/venv python3

import nntplib
import socket

HOST: str = 'your.nntp.server'
CRNM = 'comp.lang.python'
USER = 'wesley'
PASS = 'you;lNeverGuess'


def main():

    try:
        n = nntplib.NNTP(HOST)
        #,  user=USER, password=PASS)
    except socket.gaierror as e:
        print("ERROR: cannot reach host '%s'" % HOST)
        print("(%s)'" % eval(str(e))[1])
        return
    except nntplib.NNTPPermanentError as e:
        print("ERROR: access denied on '%s'" % HOST)
        print("'%s'" % str(e))
        return
    print("*** Connected to host '%s'" % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(CRNM)
    except nntplib.NNTPPermanentError as ee:
        print("ERROR: cannot load group '%s'" % CRNM)
        print("('%s')" % str(ee))
        print('Server may require authentication')
        print('Uncomment/edit login line above')
        n.quit()
        return
    except nntplib.NNTPTemporaryError as ee:
        print("ERROR: group '%s' unavailable" % CRNM)
        print("('%s')" % str(e))
        n.quit()
        return
    print("*** Found newsgroup '%s'" % CRNM)

    rng = '%s-%s' % (lst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print('''*** Found last article (#%s):
            
             from: %s
             subject: %s
             Date: %s
          ''' % (lst, frm[0][1], sub[0][1], dat[0][1]))

    rspm, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    print('*** First (<20) meaningful lines:\n')
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not \
                    lower.startswith('>>>') or \
                    lower.startswith('|') or \
                    lower.startswith('in article') or \
                    lower.endswith('writes:') or \
                    lower.endswith('wrote:')):
                continue
            if not lastBlank or (lastBlank and line):
                print("    %s" % line)
                if line:
                    count += 1
                    lastBlank = False
                else:
                    lastBlank = True
            if count == 20:
                break


if __name__ == '__main__':
    main()



