templete = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1144</width>
    <height>794</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>CodeMaster</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="minimumSize">
    <size>
     <width>1129</width>
     <height>739</height>
    </size>
   </property>
   <property name="maximumSize">
    <size>
     <width>1167</width>
     <height>16777215</height>
    </size>
   </property>
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <widget class="QSplitter" name="horSplitter">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <widget class="QTreeView" name="treeView">
       <property name="headerHidden">
        <bool>true</bool>
       </property>
      </widget>
      <widget class="QSplitter" name="vertSplitter">
       <property name="orientation">
        <enum>Qt::Vertical</enum>
       </property>
       <widget class="QTabWidget" name="tabWidget">
        <property name="currentIndex">
         <number>-1</number>
        </property>
        <property name="tabsClosable">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QTextEdit" name="output">
        <property name="font">
         <font>
          <pointsize>16</pointsize>
         </font>
        </property>
        <property name="placeholderText">
         <string>Результат выполнения кода</string>
        </property>
       </widget>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1144</width>
     <height>21</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuFile">
    <property name="title">
     <string>Файл</string>
    </property>
    <addaction name="actionNew"/>
    <addaction name="actionOpen"/>
    <addaction name="actionOpen_folder"/>
    <addaction name="separator"/>
    <addaction name="actionSave"/>
    <addaction name="actionSave_as"/>
    <addaction name="actionSave_all"/>
    <addaction name="separator"/>
    <addaction name="actionClose"/>
    <addaction name="actionExit"/>
   </widget>
   <widget class="QMenu" name="menuHelp">
    <property name="title">
     <string>Помощь</string>
    </property>
    <addaction name="actionAbout_CodeMaster"/>
   </widget>
   <widget class="QMenu" name="menuRun">
    <property name="title">
     <string>Запуск</string>
    </property>
    <addaction name="actionRun_file"/>
    <addaction name="actionRun_project"/>
    <addaction name="actionConfigure_runner"/>
   </widget>
   <addaction name="menuFile"/>
   <addaction name="menuRun"/>
   <addaction name="menuHelp"/>
  </widget>
  <widget class="QToolBar" name="toolBar">
   <property name="windowTitle">
    <string>toolBar</string>
   </property>
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
   <addaction name="actionNew"/>
   <addaction name="actionOpen"/>
   <addaction name="actionOpen_folder"/>
   <addaction name="actionSave_all"/>
   <addaction name="actionSave_as"/>
  </widget>
  <widget class="QToolBar" name="toolBar_2">
   <property name="windowTitle">
    <string>toolBar_2</string>
   </property>
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
   <addaction name="actionRun_file"/>
   <addaction name="actionConfigure_runner"/>
  </widget>
  <action name="actionOpen">
   <property name="icon">
    <iconset>
     <normaloff>icons/open_file.png</normaloff>icons/open_file.png</iconset>
   </property>
   <property name="text">
    <string>Открыть</string>
   </property>
  </action>
  <action name="actionSave">
   <property name="icon">
    <iconset>
     <normaloff>icons/save.png</normaloff>icons/save.png</iconset>
   </property>
   <property name="text">
    <string>Сохранить</string>
   </property>
  </action>
  <action name="actionSave_as">
   <property name="icon">
    <iconset>
     <normaloff>icons/save_as.png</normaloff>icons/save_as.png</iconset>
   </property>
   <property name="text">
    <string>Сохранить как</string>
   </property>
  </action>
  <action name="actionSave_all">
   <property name="icon">
    <iconset>
     <normaloff>icons/save.png</normaloff>icons/save.png</iconset>
   </property>
   <property name="text">
    <string>Сохранить все</string>
   </property>
  </action>
  <action name="actionClose">
   <property name="icon">
    <iconset>
     <normaloff>icons/close.png</normaloff>icons/close.png</iconset>
   </property>
   <property name="text">
    <string>Закрыть файл</string>
   </property>
  </action>
  <action name="actionExit">
   <property name="icon">
    <iconset>
     <normaloff>icons/exit.png</normaloff>icons/exit.png</iconset>
   </property>
   <property name="text">
    <string>Выйти</string>
   </property>
  </action>
  <action name="actionUndo">
   <property name="text">
    <string>Undo</string>
   </property>
  </action>
  <action name="actionRedo">
   <property name="text">
    <string>Redo</string>
   </property>
  </action>
  <action name="actionCut">
   <property name="text">
    <string>Cut</string>
   </property>
  </action>
  <action name="actionCopy">
   <property name="text">
    <string>Copy</string>
   </property>
  </action>
  <action name="actionSelect_all">
   <property name="text">
    <string>Select all</string>
   </property>
  </action>
  <action name="actionAbout_CodeMaster">
   <property name="icon">
    <iconset>
     <normaloff>icons/about.png</normaloff>icons/about.png</iconset>
   </property>
   <property name="text">
    <string>О программе</string>
   </property>
  </action>
  <action name="actionNew">
   <property name="icon">
    <iconset>
     <normaloff>icons/new.png</normaloff>icons/new.png</iconset>
   </property>
   <property name="text">
    <string>Новый файл</string>
   </property>
  </action>
  <action name="actionOpen_folder">
   <property name="icon">
    <iconset>
     <normaloff>icons/open_folder.png</normaloff>icons/open_folder.png</iconset>
   </property>
   <property name="text">
    <string>Открыть папку</string>
   </property>
  </action>
  <action name="actionRun_file">
   <property name="icon">
    <iconset>
     <normaloff>icons/run (2).png</normaloff>icons/run (2).png</iconset>
   </property>
   <property name="text">
    <string>Запустить файл</string>
   </property>
  </action>
  <action name="actionRun_project">
   <property name="text">
    <string>Запустить проект</string>
   </property>
  </action>
  <action name="actionConfigure_runner">
   <property name="icon">
    <iconset>
     <normaloff>icons/configurate.png</normaloff>icons/configurate.png</iconset>
   </property>
   <property name="text">
    <string>Конфигурация программ запуска</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
"""