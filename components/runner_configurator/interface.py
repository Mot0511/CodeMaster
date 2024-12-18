template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>655</width>
    <height>395</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Конфигурация программ запуска</string>
  </property>
  <layout class="QGridLayout" name="gridLayout">
   <item row="0" column="0">
    <widget class="QGroupBox" name="groupBox">
     <property name="title">
      <string>Программы запуска для одиночных файлов</string>
     </property>
     <layout class="QGridLayout" name="gridLayout_2">
      <item row="0" column="0">
       <widget class="QTableWidget" name="table"/>
      </item>
      <item row="1" column="0">
       <widget class="QPushButton" name="addBtn">
        <property name="text">
         <string>Добавить программу запуска</string>
        </property>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
   <item row="4" column="0">
    <widget class="QDialogButtonBox" name="buttonBox">
     <property name="orientation">
      <enum>Qt::Horizontal</enum>
     </property>
     <property name="standardButtons">
      <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
     </property>
    </widget>
   </item>
   <item row="3" column="0">
    <widget class="QGroupBox" name="groupBox_2">
     <property name="title">
      <string>Команда для запуска целого проекта</string>
     </property>
     <layout class="QGridLayout" name="gridLayout_3">
      <item row="0" column="0">
       <widget class="QLineEdit" name="runCommand">
        <property name="placeholderText">
         <string>Команда (например, &quot;npm run dev&quot;)</string>
        </property>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>buttonBox</sender>
   <signal>rejected()</signal>
   <receiver>Dialog</receiver>
   <slot>reject()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>316</x>
     <y>260</y>
    </hint>
    <hint type="destinationlabel">
     <x>286</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>buttonBox</sender>
   <signal>accepted()</signal>
   <receiver>Dialog</receiver>
   <slot>accept()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>248</x>
     <y>254</y>
    </hint>
    <hint type="destinationlabel">
     <x>157</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
"""