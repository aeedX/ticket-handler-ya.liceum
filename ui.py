admins = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>250</width>
    <height>290</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QLineEdit" name="user_login">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>150</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>логин</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_admin_add">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>30</y>
     <width>70</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>добавить</string>
   </property>
  </widget>
  <widget class="QTableWidget" name="table_admins">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>70</y>
     <width>151</width>
     <height>181</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_cancel">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>260</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>отменить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_save">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>260</y>
     <width>70</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>сохранить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_admin_del">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>70</y>
     <width>70</width>
     <height>35</height>
    </rect>
   </property>
   <property name="text">
    <string>удалить
выбранного</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>0</y>
     <width>231</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

categories = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>250</width>
    <height>290</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QLineEdit" name="cat_name">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>150</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Название категории</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_cat_add">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>30</y>
     <width>70</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>добавить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_cancel">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>260</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>отменить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_save">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>260</y>
     <width>70</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>сохранить</string>
   </property>
  </widget>
  <widget class="QTableWidget" name="table_cat">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>70</y>
     <width>151</width>
     <height>181</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_cat_del">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>70</y>
     <width>70</width>
     <height>35</height>
    </rect>
   </property>
   <property name="text">
    <string>удалить
выбранное</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>0</y>
     <width>231</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

close_dialog = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>230</width>
    <height>100</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>0</y>
     <width>211</width>
     <height>61</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Вы точно хотите закрыть
это обращение?</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_y">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>60</y>
     <width>80</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>да</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_n">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>60</y>
     <width>80</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>нет</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

create = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>360</width>
    <height>190</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="btn_cancel">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>160</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>отменить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_save">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>160</y>
     <width>81</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>сохранить</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="heading">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>200</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>заголовок</string>
   </property>
  </widget>
  <widget class="QComboBox" name="cb_category">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>40</y>
     <width>131</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>10</y>
     <width>101</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Категория:</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_img">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>80</y>
     <width>131</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>Выбрать фото ...</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_img">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>110</y>
     <width>130</width>
     <height>70</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>../data/img-placeholder.png</pixmap>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="desc">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>50</y>
     <width>201</width>
     <height>101</height>
    </rect>
   </property>
   <property name="plainText">
    <string>описание</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

login = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>343</width>
    <height>248</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QTabWidget" name="tabWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>341</width>
     <height>241</height>
    </rect>
   </property>
   <property name="currentIndex">
    <number>0</number>
   </property>
   <widget class="QWidget" name="tab">
    <attribute name="title">
     <string>вход</string>
    </attribute>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>331</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>16</pointsize>
      </font>
     </property>
     <property name="text">
      <string>Вход в аккаунт</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLineEdit" name="username">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>70</y>
       <width>170</width>
       <height>20</height>
      </rect>
     </property>
     <property name="inputMethodHints">
      <set>Qt::ImhNone</set>
     </property>
     <property name="inputMask">
      <string/>
     </property>
     <property name="text">
      <string>логин</string>
     </property>
     <property name="maxLength">
      <number>32767</number>
     </property>
    </widget>
    <widget class="QPushButton" name="btn_login">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>140</y>
       <width>171</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>войти</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="pas">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>100</y>
       <width>171</width>
       <height>20</height>
      </rect>
     </property>
     <property name="inputMask">
      <string/>
     </property>
     <property name="text">
      <string>пароль</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_status">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>30</y>
       <width>331</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="text">
      <string>введите логин и пароль</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="tab_2">
    <attribute name="title">
     <string>регистрация</string>
    </attribute>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>331</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>16</pointsize>
      </font>
     </property>
     <property name="text">
      <string>Регистрация</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="label_reg_status">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>30</y>
       <width>331</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="text">
      <string>придумайте логин и пароль </string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLineEdit" name="reg_username">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>70</y>
       <width>171</width>
       <height>20</height>
      </rect>
     </property>
     <property name="inputMask">
      <string/>
     </property>
     <property name="text">
      <string>логин</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="reg_pas">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>100</y>
       <width>171</width>
       <height>20</height>
      </rect>
     </property>
     <property name="inputMask">
      <string/>
     </property>
     <property name="text">
      <string>пароль</string>
     </property>
    </widget>
    <widget class="QPushButton" name="btn_reg">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>170</y>
       <width>171</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>зарегистрироваться</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="reg_pas_confirm">
     <property name="geometry">
      <rect>
       <x>80</x>
       <y>130</y>
       <width>171</width>
       <height>20</height>
      </rect>
     </property>
     <property name="inputMask">
      <string/>
     </property>
     <property name="text">
      <string>подтверждение пароля</string>
     </property>
    </widget>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

main_page = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>460</width>
    <height>340</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>460</width>
      <height>320</height>
     </rect>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="tab_user">
     <attribute name="title">
      <string>пользователь</string>
     </attribute>
     <widget class="QLabel" name="label">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>131</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>12</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Мои обращения</string>
      </property>
     </widget>
     <widget class="QPushButton" name="btn_add">
      <property name="geometry">
       <rect>
        <x>350</x>
        <y>0</y>
        <width>100</width>
        <height>23</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>8</pointsize>
       </font>
      </property>
      <property name="text">
       <string>добавить</string>
      </property>
     </widget>
     <widget class="QTableWidget" name="user_table">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>30</y>
        <width>451</width>
        <height>251</height>
       </rect>
      </property>
     </widget>
     <widget class="QPushButton" name="btn_update">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>0</y>
        <width>100</width>
        <height>23</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>8</pointsize>
       </font>
      </property>
      <property name="text">
       <string>обновить</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_admin">
     <attribute name="title">
      <string>администратор</string>
     </attribute>
     <widget class="QLabel" name="label_2">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>101</width>
        <height>25</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>12</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Обращения</string>
      </property>
     </widget>
     <widget class="QComboBox" name="cb_sorting">
      <property name="geometry">
       <rect>
        <x>340</x>
        <y>30</y>
        <width>110</width>
        <height>25</height>
       </rect>
      </property>
      <property name="currentText">
       <string>сначала старые</string>
      </property>
      <item>
       <property name="text">
        <string>сначала старые</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>сначала новые</string>
       </property>
      </item>
     </widget>
     <widget class="QPushButton" name="btn_categories">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>265</y>
        <width>160</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>редактировать категории</string>
      </property>
     </widget>
     <widget class="QPushButton" name="btn_admins">
      <property name="geometry">
       <rect>
        <x>220</x>
        <y>265</y>
        <width>110</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>администраторы</string>
      </property>
     </widget>
     <widget class="QTableWidget" name="admin_table">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>30</y>
        <width>331</width>
        <height>231</height>
       </rect>
      </property>
     </widget>
     <widget class="QPushButton" name="btn_admin_update">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>0</y>
        <width>100</width>
        <height>23</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>8</pointsize>
       </font>
      </property>
      <property name="text">
       <string>обновить</string>
      </property>
     </widget>
     <widget class="QWidget" name="verticalLayoutWidget">
      <property name="geometry">
       <rect>
        <x>339</x>
        <y>60</y>
        <width>111</width>
        <height>65</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QCheckBox" name="checkBox_waiting">
         <property name="text">
          <string>в обработке</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="checkBox_reviewed">
         <property name="text">
          <string> рассмотрено</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="checkBox_closed">
         <property name="text">
          <string>закрыто</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QComboBox" name="cb_cat_sorting">
      <property name="geometry">
       <rect>
        <x>340</x>
        <y>130</y>
        <width>110</width>
        <height>25</height>
       </rect>
      </property>
      <property name="currentText">
       <string/>
      </property>
     </widget>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>460</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="actionqwe">
   <property name="text">
    <string>qwe</string>
   </property>
  </action>
  <action name="action_4">
   <property name="text">
    <string>пользователь</string>
   </property>
  </action>
  <action name="action_5">
   <property name="text">
    <string>администратор</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

ticket_edit = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>603</width>
    <height>254</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>71</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Заголовок:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>100</y>
     <width>61</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Описание:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_5">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>10</y>
     <width>81</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Категория:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="heading">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>50</y>
     <width>201</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>заголовок</string>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>10</y>
     <width>61</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Статус:</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="rb_waiting">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>420</x>
     <y>30</y>
     <width>121</width>
     <height>17</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>в обработке</string>
   </property>
   <property name="checkable">
    <bool>true</bool>
   </property>
   <property name="checked">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QRadioButton" name="rb_reviewed">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>420</x>
     <y>50</y>
     <width>121</width>
     <height>17</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>рассмотрено</string>
   </property>
   <property name="checkable">
    <bool>true</bool>
   </property>
   <property name="checked">
    <bool>false</bool>
   </property>
   <property name="autoRepeat">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QRadioButton" name="rb_closed">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>420</x>
     <y>70</y>
     <width>121</width>
     <height>17</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>закрыто</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_4">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>70</y>
     <width>91</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>В обработке:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_timer">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>90</y>
     <width>151</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>0 часов</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_8">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>130</y>
     <width>141</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Ответ представителя:</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_close_cancel">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>220</y>
     <width>90</width>
     <height>23</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>закрыть</string>
   </property>
  </widget>
  <widget class="QPushButton" name="btn_delete_save">
   <property name="geometry">
    <rect>
     <x>124</x>
     <y>220</y>
     <width>90</width>
     <height>23</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>удалить</string>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="description">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>120</y>
     <width>201</width>
     <height>91</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
   <property name="plainText">
    <string>описание</string>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="answer">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>150</y>
     <width>161</width>
     <height>91</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
   <property name="plainText">
    <string>ответ
</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_date">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>0</y>
     <width>101</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>21.11.2024 23:59</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="label_category">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>30</y>
     <width>141</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>другое</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_user">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>0</y>
     <width>91</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>user</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="label_6">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>110</y>
     <width>101</width>
     <height>16</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Изображение:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_img">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>140</y>
     <width>180</width>
     <height>101</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
