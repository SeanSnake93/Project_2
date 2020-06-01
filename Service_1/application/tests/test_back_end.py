import unittest
from flask import abort, url_for
from flask_testing import TestCase
from application import app

# ---------- Base-SetUp-Testing ----------

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app

class TestViews(TestBase):
    def test_homepage_view(self):
        """This is the server getting a status code 200"""
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

# -------- END-Visit-Testing --------

# ____________________________________________________________________

# Users has been preserved for possible expantion of a users table. May
# be made using Docker insetead of SQL.

# ---------- Create-Function-Testing ----------

# class TestRegUserF(TestBase):
#     def test_accadd_user(self):
#         """This is to add a User to the database"""
#         with self.client:
#             self.client.post(
#                 url_for('register'),
#                 data=dict(
#                     first_name="NewSystem",
#                     last_name="Testing",
#                     email="NewSystem@Testing.com",
#                     password="N3wSy5temT35t1n8",
#                     confirm_password="N3wSy5temT35t1n8"
#                 )
#             )
#             follow_redirects=True
#         self.assertEqual(Users.query.count(), 3)
# 
# -------- Create-Function-Limitations --------



# -------- END-Create-Function-Testing --------

# ____________________________________________________________________

# ---------- Read-Function-Testing ----------



# -------- END-Read-Function-Testing --------

# ____________________________________________________________________

# ---------- Update-Function-Testing ----------

# class TestEditUserF(TestBase):
#    def test_edit_user(self):
#        """This is to Edit a User to the database 'System@Testing.com's first name from 'System' to 'BetaSystem' with this test"""
 #       with self.client:
  #          self.client.post(
   #             url_for('login'),
    #            data=dict(
     #               email="System@Testing.com",
      #              password="Sy5temT35t1n8"
       #         ),
        #    follow_redirects=True
         #   )
          #  response = self.client.post(
           #     url_for('account'),
            #    data=dict(
             #       first_name="BetaSystem",
              #      last_name="Testing",
               #     email="System@Testing.com"
                #),
#                follow_redirects=True
 #           )
  #      self.assertEqual(Users.query.filter_by(first_name="BetaSystem").count(), 1)
   #     self.assertEqual(Users.query.count(), 2)

# -------- Update-Function-Limitations --------

# -------- END-Update-Function-Testing --------

# ____________________________________________________________________

# ---------- Delete-Function-Testing ----------

#class TestAccDelF(TestBase):
 #   """This as it stands will fail as the item is able to be duplicated in the current system"""
  #  def test_accdel_user(self):
   #     with self.client:
    #        self.client.post(
     #           url_for('login'),
      #          data=dict(
       #             email="System@Testing.com",
        #            password="Sy5temT35t1n8"
         #       ),
          #  follow_redirects=True
           # )
            #response = self.client.post(
             #   url_for('add_collection', film=1),
              #  follow_redirects=True
#            )
 #           self.assertEqual(Collection.query.filter_by(user_id=2).count(), 1)

#            response = self.client.post(
 #               url_for('account_delete'),
  #              follow_redirects=True
            )
        
   #     self.assertEqual(Collection.query.count(), 0)
    #    self.assertEqual(Users.query.count(), 1)

# -------- END-Delete-Function-Testing --------