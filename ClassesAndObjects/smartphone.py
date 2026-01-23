from contact import Contact
from contact_list import Contact_List

book = Contact_List()

book.add_contact(Contact('John Brown', 'brown@onet.pl', '555234000'))
book.add_contact(Contact('Anna May', 'am@o2.pl', '232000199'))
book.add_contact(Contact('George Small', 'smallg@google.pl', '222999100'))
book.add_contact(Contact('Paola Big', 'bigpaola@poczta.pl', '100200300'))

book.display_contacts()