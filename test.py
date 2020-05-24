def dashatize(num):
    return ''.join(['-%s-' % (i) if int(i)%2 else i for i in str(num) ]).strip('-').replace('--','-')

print(dashatize(2134))