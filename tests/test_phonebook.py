"""
This test contains tests for adding contacts, updating, delete and view contacts"""
from unittest import TestCase
from phonebook import Contacts, CONTACTS 


CONTACT = Contacts()

class ContactsTestCase(TestCase):
    def setUp(self):
        CONTACTS.clear()
        self.name = "Lawrence"
        self.phone = "0708686842"
    
    def test_Add_contact(self):
        """tests that a new contact can be added successfully"""
        self.assertIsInstance(CONTACT,Contacts)
        self.assertTrue(len(CONTACTS) == 0)
        response = CONTACT.Add_contact('james','0709686842')
        self.assertTrue(len(CONTACTS) > 0)
        self.assertEqual(response ['name'],"james")
        duplicate = CONTACT.Add_contact('james','0708978765')
        self.assertEqual(duplicate, " Contact already exists")

    def test_View_contact(self):
        """test if a contact can be retrieved"""
        CONTACT.Add_contact('mary', '0705678543')
        seek = CONTACT.View_contact('mary')
        self.assertEqual(seek['name'],'mary')
        seek = CONTACT.View_contact('wahu')
        self.assertEqual(seek, 'Contact does not exist')

    def test_Update_contact(self):
        """test if contact can be updated"""
        update = CONTACT.Update_contact('kezzy','0723456765')
        self.assertEqual(update, "Contact does not exist" )
        #add to dict for test
        add = CONTACT.Add_contact('kezzy','0798765432')
        self.assertTrue(add['name'] in CONTACTS)
        update = CONTACT.Update_contact('kezzy','0723456765')
        self.assertEqual(update,"Contact Updated successfully")

    def test_Delete_contact(self):
        pass

