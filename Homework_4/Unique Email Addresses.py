email = input()

emails = email.split()

for i in range(len(emails)):
    e = emails[i]
    if '@' not in e:
        emails.pop(i)
        continue
    if '.' in e[:e.index('@')]:
        count_point = e[:e.index('@')].count('.')
        emails[i] = e.replace('.', '', count_point)
        e = emails[i]
    if '+' in e[:e.index('@')]:
        emails[i] = e.replace(e[:e.index('@')], e[:e.index('+')])


print(set(emails))
print(len(set(emails)))




