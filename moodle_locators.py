from faker import Faker
#Faker.seed(0)
fake=Faker(local='en_CA')
moodle_url='http://54.214.118.90/'
moodle_login_url="http://54.214.118.90/login/index.php"
moodle_username='admin'
moodle_password='Moodle$erver003!#'
moodle_dashboard_url='http://54.214.118.90/my/'
moodle_users_main_page='http://54.214.118.90/admin/user.php'

new_username=f"{fake.lexify('??', letters='abcdefghijklmnopqrstuvwxyz')}{fake.user_name()}"
new_password=fake.password()
buffer_username=new_username
buffer_password=new_password
first_name=fake.first_name()
last_name=fake.last_name()
email=f'{fake.lexify(text="??")}{fake.email()}'
moodle_net_profile=f'https://moodle.net/{new_username}'

city=fake.city()
country=fake.country()
desc=fake.sentence(nb_words=255)
#description = fake.text(1000)
pic_desc=new_username
phonetic_first_name=fake.first_name()
phonetic_last_name=fake.last_name()
phonetic_middle_name=fake.first_name()
phonetic_alternate_name=f'{fake.last_name()}'+f'{fake.first_name()}'
#OR:
#phonetic_alternate_name=f'{fake.last_name()}{fake.first_name()}'
list_of_interests=[fake.word(),fake.password(),fake.word(),fake.text(30),fake.text(30),fake.word()]
id_number=fake.pyint(11111111,99999999)
institution=f'{fake.word()}{fake.pyint(111111,999999)}'
phone1=fake.phone_number()
phone2=fake.phone_number()
#department=fake.lexify(text='????') # for letters only; numerify(), fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^', upper=True)
department=fake.bothify(text='%%????')
address=fake.address().replace('\n', ';')
fullname=f'{first_name}'+' '+f'{last_name}'
#fullname=f'{first_name} {last_name}'
