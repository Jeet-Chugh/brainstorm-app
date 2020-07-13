# Essential Kivy Imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
# Widget Imports
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
# Other Imports
import pickle
import os.path
from collections import defaultdict

class Create_Screen(Screen):
    def __init__(self,**kwargs):
        super(Create_Screen,self).__init__(**kwargs)

    def save_idea(self):
        # Import Data
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)
        try:
            all_ideas_list = pickle.load(open('data\\info\\all_ideas.pkl','rb'))
        except:
            all_ideas_list = ['_']

        # Assign Input Variables
        idea_name = self.ids['idea_name'].text
        idea_category = self.ids['category_name'].text.lower()
        idea_text = self.ids['idea_text'].text

        path = 'data\\ideas\\' + idea_name.replace(' ','_') + '.txt'

        # Check for Errors
        if len(idea_name) == 0:
            return app.error_popup('Error: No Name')
        elif len(idea_category) == 0:
            return app.error_popup('Error: No Category')
        elif len(idea_text) == 0:
            return app.error_popup('Error: No Text')
        elif path in all_ideas_list:
            return app.error_popup('Error: Idea Already Exists')
        elif len(category_ideas_dict[idea_category]) >= 10:
            return app.error_popup('Error: Category Full')
        elif len(list(category_ideas_dict.keys())) >= 40:
            return app.error_popup('Error: Too Many Categories')

        # Create File
        open(path,'w').write(idea_text)
        category_ideas_dict[idea_category].append(path)
        all_ideas_list.append(path)

        # Save Data
        pickle.dump(category_ideas_dict,open('data\\info\\categories_ideas.pkl','wb'))
        pickle.dump(all_ideas_list,open('data\\info\\all_ideas.pkl','wb'))

        # Update All Categories (Ideas/Categories)
        Create_Category().update_all_cats()
        Create_Category().update_all_ideas()
        app.update_recents()
        app.root.ids['create_category'].ids.category_list.text = Create_Category().category_string()

class Create_Category(Screen):
    def __init__(self,**kwargs):
        super(Create_Category,self).__init__(**kwargs)

    def create_category(self):
        # Import Data
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)

        # Create Category if it doesnt exist
        if self.ids.new_category_name.text.lower() not in list(category_ideas_dict.keys()):
            category_ideas_dict[self.ids.new_category_name.text.lower()] = []
            pickle.dump(category_ideas_dict,open('data\\info\\categories_ideas.pkl','wb'))
        else:
            app.error_popup('Category Already Exists')

        # Update All Categories
        self.ids.category_list.text = self.category_string()

        app.update_cat_list()
        self.update_all_cats()

    def delete_category(self):
        # Delete Category from List
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)
        try:
            del category_ideas_dict[self.ids.del_category_name.text]
            pickle.dump(category_ideas_dict,open('data\\info\\categories_ideas.pkl','wb'))
        except:
            app.error_popup('Error: Invalid Category')

        # Remove Deleted Categories Instance in "Recent Categories"
        for i,item in enumerate([app.root.ids['ideas_screen'].ids.a.text,app.root.ids['ideas_screen'].ids.b.text,
                     app.root.ids['ideas_screen'].ids.c.text,app.root.ids['ideas_screen'].ids.d.text,
                     app.root.ids['ideas_screen'].ids.e.text,app.root.ids['ideas_screen'].ids.f.text,
                     app.root.ids['ideas_screen'].ids.g.text,app.root.ids['ideas_screen'].ids.h.text,
                     app.root.ids['ideas_screen'].ids.i.text,app.root.ids['ideas_screen'].ids.j.text]):

            if item == self.ids.del_category_name.text:
                if i == 0:
                    app.root.ids['ideas_screen'].ids.a.text = 'N/A'
                elif i == 1:
                    app.root.ids['ideas_screen'].ids.b.text = 'N/A'
                elif i == 2:
                    app.root.ids['ideas_screen'].ids.c.text = 'N/A'
                elif i == 3:
                    app.root.ids['ideas_screen'].ids.d.text = 'N/A'
                elif i == 4:
                    app.root.ids['ideas_screen'].ids.e.text = 'N/A'
                elif i == 5:
                    app.root.ids['ideas_screen'].ids.f.text = 'N/A'
                elif i == 6:
                    app.root.ids['ideas_screen'].ids.g.text = 'N/A'
                elif i == 7:
                    app.root.ids['ideas_screen'].ids.h.text = 'N/A'
                elif i == 8:
                    app.root.ids['ideas_screen'].ids.i.text = 'N/A'
                elif i == 9:
                    app.root.ids['ideas_screen'].ids.j.text = 'N/A'

        # Category List Updating
        self.ids.category_list.text = self.category_string()
        self.update_all_cats()

    def update_all_cats(self):
        # Update the ALL CATEGORIES section
        app.root.ids['all_categories'].ids.a1.text = All_Categories().category_names(1)
        app.root.ids['all_categories'].ids.a2.text = All_Categories().category_names(2)
        app.root.ids['all_categories'].ids.a3.text = All_Categories().category_names(3)
        app.root.ids['all_categories'].ids.a4.text = All_Categories().category_names(4)
        app.root.ids['all_categories'].ids.a5.text = All_Categories().category_names(5)
        app.root.ids['all_categories'].ids.a6.text = All_Categories().category_names(6)
        app.root.ids['all_categories'].ids.a7.text = All_Categories().category_names(7)
        app.root.ids['all_categories'].ids.a8.text = All_Categories().category_names(8)
        app.root.ids['all_categories'].ids.a9.text = All_Categories().category_names(9)
        app.root.ids['all_categories'].ids.a10.text = All_Categories().category_names(10)
        app.root.ids['all_categories'].ids.a11.text = All_Categories().category_names(11)
        app.root.ids['all_categories'].ids.a12.text = All_Categories().category_names(12)
        app.root.ids['all_categories'].ids.a13.text = All_Categories().category_names(13)
        app.root.ids['all_categories'].ids.a14.text = All_Categories().category_names(14)
        app.root.ids['all_categories'].ids.a15.text = All_Categories().category_names(15)
        app.root.ids['all_categories'].ids.a16.text = All_Categories().category_names(16)
        app.root.ids['all_categories'].ids.a17.text = All_Categories().category_names(17)
        app.root.ids['all_categories'].ids.a18.text = All_Categories().category_names(18)
        app.root.ids['all_categories'].ids.a19.text = All_Categories().category_names(19)
        app.root.ids['all_categories'].ids.a20.text = All_Categories().category_names(20)
        app.root.ids['all_categories'].ids.a21.text = All_Categories().category_names(21)
        app.root.ids['all_categories'].ids.a22.text = All_Categories().category_names(22)
        app.root.ids['all_categories'].ids.a23.text = All_Categories().category_names(23)
        app.root.ids['all_categories'].ids.a24.text = All_Categories().category_names(24)
        app.root.ids['all_categories'].ids.a25.text = All_Categories().category_names(25)
        app.root.ids['all_categories'].ids.a26.text = All_Categories().category_names(26)
        app.root.ids['all_categories'].ids.a27.text = All_Categories().category_names(27)
        app.root.ids['all_categories'].ids.a28.text = All_Categories().category_names(28)
        app.root.ids['all_categories'].ids.a29.text = All_Categories().category_names(29)
        app.root.ids['all_categories'].ids.a30.text = All_Categories().category_names(30)
        app.root.ids['all_categories'].ids.a31.text = All_Categories().category_names(31)
        app.root.ids['all_categories'].ids.a32.text = All_Categories().category_names(32)
        app.root.ids['all_categories'].ids.a33.text = All_Categories().category_names(33)
        app.root.ids['all_categories'].ids.a34.text = All_Categories().category_names(34)
        app.root.ids['all_categories'].ids.a35.text = All_Categories().category_names(35)
        app.root.ids['all_categories'].ids.a36.text = All_Categories().category_names(36)
        app.root.ids['all_categories'].ids.a37.text = All_Categories().category_names(37)
        app.root.ids['all_categories'].ids.a38.text = All_Categories().category_names(38)
        app.root.ids['all_categories'].ids.a39.text = All_Categories().category_names(39)
        app.root.ids['all_categories'].ids.a40.text = All_Categories().category_names(40)

    def update_all_ideas(self):
        # Update the ALL IDEAS Section
        app.root.ids['all_ideas'].ids.b1.text = All_Ideas().ideas_names(1)
        app.root.ids['all_ideas'].ids.b2.text = All_Ideas().ideas_names(2)
        app.root.ids['all_ideas'].ids.b3.text = All_Ideas().ideas_names(3)
        app.root.ids['all_ideas'].ids.b4.text = All_Ideas().ideas_names(4)
        app.root.ids['all_ideas'].ids.b5.text = All_Ideas().ideas_names(5)
        app.root.ids['all_ideas'].ids.b6.text = All_Ideas().ideas_names(6)
        app.root.ids['all_ideas'].ids.b7.text = All_Ideas().ideas_names(7)
        app.root.ids['all_ideas'].ids.b8.text = All_Ideas().ideas_names(8)
        app.root.ids['all_ideas'].ids.b9.text = All_Ideas().ideas_names(9)
        app.root.ids['all_ideas'].ids.b10.text = All_Ideas().ideas_names(10)
        app.root.ids['all_ideas'].ids.b11.text = All_Ideas().ideas_names(11)
        app.root.ids['all_ideas'].ids.b12.text = All_Ideas().ideas_names(12)
        app.root.ids['all_ideas'].ids.b13.text = All_Ideas().ideas_names(13)
        app.root.ids['all_ideas'].ids.b14.text = All_Ideas().ideas_names(14)
        app.root.ids['all_ideas'].ids.b15.text = All_Ideas().ideas_names(15)
        app.root.ids['all_ideas'].ids.b16.text = All_Ideas().ideas_names(16)
        app.root.ids['all_ideas'].ids.b17.text = All_Ideas().ideas_names(17)
        app.root.ids['all_ideas'].ids.b18.text = All_Ideas().ideas_names(18)
        app.root.ids['all_ideas'].ids.b19.text = All_Ideas().ideas_names(19)
        app.root.ids['all_ideas'].ids.b20.text = All_Ideas().ideas_names(20)
        app.root.ids['all_ideas'].ids.b21.text = All_Ideas().ideas_names(21)
        app.root.ids['all_ideas'].ids.b22.text = All_Ideas().ideas_names(22)
        app.root.ids['all_ideas'].ids.b23.text = All_Ideas().ideas_names(23)
        app.root.ids['all_ideas'].ids.b24.text = All_Ideas().ideas_names(24)
        app.root.ids['all_ideas'].ids.b25.text = All_Ideas().ideas_names(25)
        app.root.ids['all_ideas'].ids.b26.text = All_Ideas().ideas_names(26)
        app.root.ids['all_ideas'].ids.b27.text = All_Ideas().ideas_names(27)
        app.root.ids['all_ideas'].ids.b28.text = All_Ideas().ideas_names(28)
        app.root.ids['all_ideas'].ids.b29.text = All_Ideas().ideas_names(29)
        app.root.ids['all_ideas'].ids.b30.text = All_Ideas().ideas_names(30)
        app.root.ids['all_ideas'].ids.b31.text = All_Ideas().ideas_names(31)
        app.root.ids['all_ideas'].ids.b32.text = All_Ideas().ideas_names(32)
        app.root.ids['all_ideas'].ids.b33.text = All_Ideas().ideas_names(33)
        app.root.ids['all_ideas'].ids.b34.text = All_Ideas().ideas_names(34)
        app.root.ids['all_ideas'].ids.b35.text = All_Ideas().ideas_names(35)
        app.root.ids['all_ideas'].ids.b36.text = All_Ideas().ideas_names(36)
        app.root.ids['all_ideas'].ids.b37.text = All_Ideas().ideas_names(37)
        app.root.ids['all_ideas'].ids.b38.text = All_Ideas().ideas_names(38)
        app.root.ids['all_ideas'].ids.b39.text = All_Ideas().ideas_names(39)
        app.root.ids['all_ideas'].ids.b40.text = All_Ideas().ideas_names(40)

    def category_string(self):
        # Make the categories string
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)

        catstring = ', '.join(list(category_ideas_dict.keys()))
        return str(catstring)

class View_Category(Screen):
    def __init__(self,**kwargs):
        super(View_Category,self).__init__(**kwargs)

    def ideas_in_x(self):
        # Secondary Header for View Category Section
        return('Ideas in {a}'.format(a=self.ids['category_name'].text))

class View_Idea(Screen):
    def __init__(self,**kwargs):
        super(View_Idea,self).__init__(**kwargs)

    def edit_idea(self):
        path = 'data\\ideas\\' + self.ids['idea_name_label'].text.replace(' ','_') + '.txt'
        open(path,'w').write(self.ids['idea_text_edit'].text)

    def delete_idea(self):

        app.root.ids['screen_manager'].current = 'ideas_screen'
        recent_ideas_list = pickle.load(open('data\\info\\all_ideas.pkl','rb'))
        category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        path = path = 'data\\ideas\\' + self.ids['idea_name_label'].text.replace(' ','_') + '.txt'

        for value in list(category_ideas_dict.values()):
            if path in value:
                del_value = value
                break
            else:
                del_value = None
        try:
            if del_value != None:
                del_key = [key for (key,val) in category_ideas_dict.items() if val == del_value][0]
                category_ideas_dict[del_key].remove(path)
        except:  pass

        if path in recent_ideas_list:
            recent_ideas_list.remove(path)

        if os.path.exists(path):
            os.remove(path)
        else:
            app.error_popup('Something Went Wrong!')

        pickle.dump(category_ideas_dict,open('data\\info\\categories_ideas.pkl','wb'))
        pickle.dump(recent_ideas_list,open('data\\info\\all_ideas.pkl','wb'))

        Create_Category().update_all_cats()
        Create_Category().update_all_ideas()
        app.update_recents()
        app.root.ids['create_category'].ids.category_list.text = Create_Category().category_string()

class All_Categories(Screen):
    def __init__(self,**kwargs):
        super(All_Categories,self).__init__(**kwargs)

    def category_names(self,i):
        # Return First Category In Section
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)
        try:
            a = list(category_ideas_dict.keys())[i-1]
            return a
        except:
            return ''

class All_Ideas(Screen):
    def __init__(self,**kwargs):
        super(All_Ideas,self).__init__(**kwargs)

    def ideas_names(self,i):
        try:
            all_ideas_list = pickle.load(open('data\\info\\all_ideas.pkl','rb'))
        except:
            all_ideas_list = ['_']
        try:
            a = all_ideas_list[1:]
            return a[i-1].replace('data\\ideas\\','').replace('.txt','').replace('_',' ')
        except:
            return ''


class Ideas_Screen(Screen):
    def __init__(self,**kwargs):
        super(Ideas_Screen,self).__init__(**kwargs)

    def recent_text(self,i):
        try:
            all_ideas_list = pickle.load(open('data\\info\\all_ideas.pkl','rb'))
        except:
            all_ideas_list = ['_']
        finally:

            try:
                a = all_ideas_list[1:]
                return a[-i].replace('data\\ideas\\','').replace('.txt','').replace('_',' ')
            except:
                return ''

    def categories_list(self,i):
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)
        try:
            a = list(category_ideas_dict.keys())[-i]
            return a
        except:
            return ''

    def view_category(self,id):
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)

        if id == '' or id not in list(category_ideas_dict.keys()):
            app.error_popup('Invalid Category')
        else:
            app.view_category(id)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

gui = Builder.load_file('main.kv')

class MainApp(App):

    def __init__(self,**kwargs):
        super(MainApp,self).__init__(**kwargs)

    def build(self):
        return gui

    def change_screen(self,screen_name):

        screen_manager = (self.root.ids['screen_manager'])
        screen_manager.current = screen_name

        change_button = {
        'create_screen' : self.root.ids.create_button,
        'ideas_screen' : self.root.ids.ideas_button,
        'settings_screen' : self.root.ids.settings_button}

        default_button = {
        'create_screen' : 'images\\buttons\\Create_Button_Normal.jpg',
        'ideas_screen' : 'images\\buttons\\Ideas_Button_Normal.jpg',
        'settings_screen' : 'images\\buttons\\Settings_Button_Normal.jpg'}

        page_names = {
        'create_screen' : 'Create',
        'ideas_screen' : 'Ideas',
        'settings_screen' : 'Settings',
        'account_settings' : 'Account',
        'notifications_settings' : 'Alerts'}

        if str(screen_manager.current) in ['create_screen','ideas_screen','settings_screen']:
            for key in change_button.keys():
                change_button[key].background_normal = default_button[key]
                change_button[str(screen_manager.current)].background_normal = str(
                default_button[screen_manager.current].replace('Normal','Down'))

    def view_idea(self,file_name):
        if file_name == '':
            return app.error_popup('Invalid Idea')
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)

        path = 'data\\ideas\\' + file_name.replace(' ','_') + '.txt'
        if os.path.exists(path) == False:
            return app.error_popup('Idea Not Found')

        for value in list(category_ideas_dict.values()):
            if path in value:
                del_value = value
                break
            else:
                del_value = None
        try:
            if del_value != None:
                del_key = [key for (key,val) in category_ideas_dict.items() if val == del_value][0]
        except:  pass

        self.root.ids['view_idea'].ids.idea_name_label.text = file_name
        self.root.ids['view_idea'].ids.idea_text_edit.text = open(path,'r').read()
        try:
            if del_value != 'None':
                self.root.ids['view_idea'].ids.category_name_i.text = [key for (key,value) in category_ideas_dict.items() if value == del_value][0]
            else:
                self.root.ids['view_idea'].ids.category_name_i.text = '<No Category>'
        except:
            self.root.ids['view_idea'].ids.category_name_i.text = '<No Category>'

        if os.path.exists(path):
            self.change_screen('view_idea')
        else:
            self.error_popup('Idea Nonexistent')

    def update_cat_list(self):
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)

        if len(list(category_ideas_dict.keys()))>0:
            self.root.ids['ideas_screen'].ids.a.text = list(category_ideas_dict.keys())[-1]
            if len(list(category_ideas_dict.keys()))>1:
                self.root.ids['ideas_screen'].ids.b.text = list(category_ideas_dict.keys())[-2]
                if len(list(category_ideas_dict.keys()))>2:
                    self.root.ids['ideas_screen'].ids.c.text = list(category_ideas_dict.keys())[-3]
                    if len(list(category_ideas_dict.keys()))>3:
                        self.root.ids['ideas_screen'].ids.d.text = list(category_ideas_dict.keys())[-4]
                        if len(list(category_ideas_dict.keys()))>4:
                            self.root.ids['ideas_screen'].ids.e.text = list(category_ideas_dict.keys())[-5]
                            if len(list(category_ideas_dict.keys()))>5:
                                self.root.ids['ideas_screen'].ids.f.text = list(category_ideas_dict.keys())[-6]
                                if len(list(category_ideas_dict.keys()))>6:
                                    self.root.ids['ideas_screen'].ids.g.text = list(category_ideas_dict.keys())[-7]
                                    if len(list(category_ideas_dict.keys()))>7:
                                        self.root.ids['ideas_screen'].ids.h.text = list(category_ideas_dict.keys())[-8]
                                        if len(list(category_ideas_dict.keys()))>8:
                                            self.root.ids['ideas_screen'].ids.i.text = list(category_ideas_dict.keys())[-9]
                                            if len(list(category_ideas_dict.keys()))>9:
                                                self.root.ids['ideas_screen'].ids.j.text = list(category_ideas_dict.keys())[-10]

    def view_category(self,name):
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)

        if name == '':
            return self.error_popup('Invalid Category')

        self.root.ids['screen_manager'].current = 'view_category'
        self.root.ids['view_category'].ids.category_name.text = name

        try:
            if len(category_ideas_dict[name])>0:
                self.root.ids['view_category'].ids.aa.text = category_ideas_dict[name][-1].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                if len(category_ideas_dict[name])>1:
                    self.root.ids['view_category'].ids.bb.text = category_ideas_dict[name][-2].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                    if len(category_ideas_dict[name])>2:
                        self.root.ids['view_category'].ids.cc.text = category_ideas_dict[name][-3].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                        if len(category_ideas_dict[name])>3:
                            self.root.ids['view_category'].ids.dd.text = category_ideas_dict[name][-4].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                            if len(category_ideas_dict[name])>4:
                                self.root.ids['view_category'].ids.ee.text = category_ideas_dict[name][-5].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                                if len(category_ideas_dict[name])>5:
                                    self.root.ids['view_category'].ids.ff.text = category_ideas_dict[name][-6].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                                    if len(category_ideas_dict[name])>6:
                                        self.root.ids['view_category'].ids.gg.text = category_ideas_dict[name][-7].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                                        if len(category_ideas_dict[name])>7:
                                            self.root.ids['view_category'].ids.hh.text = category_ideas_dict[name][-8].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                                            if len(category_ideas_dict[name])>8:
                                                self.root.ids['view_category'].ids.ii.text = category_ideas_dict[name][-9].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')
                                                if len(category_ideas_dict[name])>9:
                                                    self.root.ids['view_category'].ids.jj.text = category_ideas_dict[name][-10].replace('_',' ').replace('data\\ideas\\','').replace('.txt','')

        except:
            self.error_popup('Invalid Idea Name')
        finally:
            self.root.ids['view_category'].ids.category_label.text = 'Ideas in {a}:'.format(
            a=self.root.ids['view_category'].ids.category_name.text)

    def categories_list(self,i):
        try:
            category_ideas_dict = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))
        except:
            category_ideas_dict = defaultdict(list)
        try:
            return list(category_ideas_dict.keys())[-i]
        except:
            return ''

    def error_popup(self,text):
        popup_button = Button(text='Dismiss')
        invalid_popup = Popup(title=text,content=popup_button,size_hint=(0.7,0.7))
        popup_button.bind(on_press=lambda *args: invalid_popup.dismiss())

        return invalid_popup.open()

    def update_recents(self):
        app.root.ids['ideas_screen'].ids.aaa1.text = Ideas_Screen().recent_text(1)
        app.root.ids['ideas_screen'].ids.aaa2.text = Ideas_Screen().recent_text(2)
        app.root.ids['ideas_screen'].ids.aaa3.text = Ideas_Screen().recent_text(3)
        app.root.ids['ideas_screen'].ids.aaa4.text = Ideas_Screen().recent_text(4)
        app.root.ids['ideas_screen'].ids.aaa5.text = Ideas_Screen().recent_text(5)
        app.root.ids['ideas_screen'].ids.aaa6.text = Ideas_Screen().recent_text(6)
        app.root.ids['ideas_screen'].ids.aaa7.text = Ideas_Screen().recent_text(7)
        app.root.ids['ideas_screen'].ids.aaa8.text = Ideas_Screen().recent_text(8)
        app.root.ids['ideas_screen'].ids.aaa9.text = Ideas_Screen().recent_text(9)
        app.root.ids['ideas_screen'].ids.aaa10.text = Ideas_Screen().recent_text(10)

        app.root.ids['ideas_screen'].ids.a.text = All_Categories().category_names(1)
        app.root.ids['ideas_screen'].ids.b.text = All_Categories().category_names(2)
        app.root.ids['ideas_screen'].ids.c.text = All_Categories().category_names(3)
        app.root.ids['ideas_screen'].ids.d.text = All_Categories().category_names(4)
        app.root.ids['ideas_screen'].ids.e.text = All_Categories().category_names(5)
        app.root.ids['ideas_screen'].ids.f.text = All_Categories().category_names(6)
        app.root.ids['ideas_screen'].ids.g.text = All_Categories().category_names(7)
        app.root.ids['ideas_screen'].ids.h.text = All_Categories().category_names(8)
        app.root.ids['ideas_screen'].ids.i.text = All_Categories().category_names(9)
        app.root.ids['ideas_screen'].ids.j.text = All_Categories().category_names(10)

    def stats(self):
        ideas_list = pickle.load(open('data\\info\\all_ideas.pkl','rb'))
        cats_list = pickle.load(open('data\\info\\categories_ideas.pkl','rb'))

        app.root.ids['stats_settings'].ids['ideas_number'].text = str(len(ideas_list)-1)
        app.root.ids['stats_settings'].ids['cat_number'].text = str(len(list(cats_list.keys())))

        app.root.ids['screen_manager'].current = 'stats_settings'

    def reset(self):
        popup_button = Button(text='Confirm Reset')
        invalid_popup = Popup(title='Reset All Data?',content=popup_button,size_hint=(0.7,0.7))
        popup_button.bind(on_press=lambda *args: app.reset_real())

        return invalid_popup.open()

    def reset_real(self):
        pickle.dump(defaultdict(list),open('data\\info\\categories_ideas.pkl','wb'))
        pickle.dump(['_'],open('data\\info\\all_ideas.pkl','wb'))

if __name__ == '__main__':
    app = MainApp()
    app.run()
