'''using return'''
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
   
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)

''' Returning a dictionary'''
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} 
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix') 
print(musician)
musician = build_person('aaa', 'bbb', age='34')
print(musician)

'''Using functuin with while loop '''
def get_formatted_name(first_name, last_name):
       """Return a full name, neatly formatted."""
       full_name = first_name + ' ' + last_name
       return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = raw_input("First name: ")
    if f_name == 'q':
        break
    l_name = raw_input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
print('\nThank you.!')