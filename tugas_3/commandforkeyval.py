epstein_files_2026 = {
    'name': 'jokoxx',
    'usia': '50',
    'hoby': 'invalid acces',
    'keluarga': 'access bloacked',

 }

epstein_files_2026['life or no ?'] = 'yes',

epstein_files_2026['usia'] = '60',

print('logic sessions ')
epstein_files_2026['passwork'] = 'satu'

login_attemp1 = 'jokoxx'
password_attemp1 = 'satu'
print('all the data', epstein_files_2026)

if login_attemp1 in epstein_files_2026['name'] and epstein_files_2026['passwork'] == password_attemp1:
    print('welcome')
else: 
    print('failed')


print('==============================')
print("=====manual login=============")

manual_int = input('input your name :')
manual_pws = input('input your password: :')
ok = 'succes'
if manual_int in epstein_files_2026['usia'] and epstein_files_2026['passwork'] == manual_pws:
    print('manual login by x is {ok}')
else:
    print('error try agaisnt :') 

print("========welomem")
print('thanks')