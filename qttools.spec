#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qttools
Version  : 5.10.1
Release  : 3
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qttools-everywhere-src-5.10.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qttools-everywhere-src-5.10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qttools-bin
Requires: qttools-lib
Requires: qttools-data
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : qtbase-dev

%description
Support for interactive help is provided by the Qt Assistant application.
Developers can take advantages of the facilities it offers to display
specially-prepared documentation to users of their applications.

%package bin
Summary: bin components for the qttools package.
Group: Binaries
Requires: qttools-data

%description bin
bin components for the qttools package.


%package data
Summary: data components for the qttools package.
Group: Data

%description data
data components for the qttools package.


%package dev
Summary: dev components for the qttools package.
Group: Development
Requires: qttools-lib
Requires: qttools-bin
Requires: qttools-data
Provides: qttools-devel

%description dev
dev components for the qttools package.


%package lib
Summary: lib components for the qttools package.
Group: Libraries
Requires: qttools-data

%description lib
lib components for the qttools package.


%prep
%setup -q -n qttools-everywhere-src-5.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/assistant
/usr/bin/designer
/usr/bin/lconvert
/usr/bin/linguist
/usr/bin/lrelease
/usr/bin/lupdate
/usr/bin/pixeltool
/usr/bin/qcollectiongenerator
/usr/bin/qdbus
/usr/bin/qdbusviewer
/usr/bin/qdoc
/usr/bin/qhelpconverter
/usr/bin/qhelpgenerator
/usr/bin/qtattributionsscanner
/usr/bin/qtdiag
/usr/bin/qtpaths
/usr/bin/qtplugininfo

%files data
%defattr(-,root,root,-)
/usr/share/qt5/phrasebooks/danish.qph
/usr/share/qt5/phrasebooks/dutch.qph
/usr/share/qt5/phrasebooks/finnish.qph
/usr/share/qt5/phrasebooks/french.qph
/usr/share/qt5/phrasebooks/german.qph
/usr/share/qt5/phrasebooks/hungarian.qph
/usr/share/qt5/phrasebooks/italian.qph
/usr/share/qt5/phrasebooks/japanese.qph
/usr/share/qt5/phrasebooks/norwegian.qph
/usr/share/qt5/phrasebooks/polish.qph
/usr/share/qt5/phrasebooks/russian.qph
/usr/share/qt5/phrasebooks/spanish.qph
/usr/share/qt5/phrasebooks/swedish.qph

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/abstractdialoggui_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/abstractintrospection_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/actioneditor_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/actionprovider_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/actionrepository_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/codedialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/connectionedit_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/csshighlighter_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/deviceprofile_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/dialoggui_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/extensionfactory_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/formbuilderextra_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/formlayoutmenu_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/formwindowbase_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/grid_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/gridpanel_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/htmlhighlighter_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/iconloader_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/iconselector_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/invisible_widget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/layout_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/layoutinfo_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/lib_pch.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/metadatabase_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/morphmenu_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/newactiondialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/newformwidget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/orderdialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/plaintexteditor_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/plugindialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/pluginmanager_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/previewconfigurationwidget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/previewmanager_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/promotionmodel_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/promotiontaskmenu_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/properties_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/propertylineedit_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_command2_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_command_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_dnditem_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_dockwidget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_formbuilder_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_formeditorcommand_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_formwindowcommand_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_formwindowmanager_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_introspection_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_membersheet_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_menu_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_menubar_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_objectinspector_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_promotion_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_promotiondialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_propertycommand_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_propertyeditor_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_propertysheet_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_qsettings_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_stackedbox_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_tabwidget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_taskmenu_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_toolbar_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_toolbox_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_utils_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_widget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_widgetbox_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qdesigner_widgetitem_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qlayout_widget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qsimpleresource_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qtresourceeditordialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qtresourcemodel_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/qtresourceview_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/rcc_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/resourcebuilder_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/richtexteditor_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/selectsignaldialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/shared_enums_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/shared_global_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/shared_settings_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/sheet_delegate_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/signalslotdialog_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/spacer_widget_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/stylesheeteditor_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/textbuilder_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/textpropertyeditor_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/ui4_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/widgetdatabase_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/widgetfactory_p.h
/usr/include/qt5/QtDesigner/5.10.1/QtDesigner/private/zoomwidget_p.h
/usr/include/qt5/QtDesigner/QAbstractExtensionFactory
/usr/include/qt5/QtDesigner/QAbstractExtensionManager
/usr/include/qt5/QtDesigner/QAbstractFormBuilder
/usr/include/qt5/QtDesigner/QDesignerActionEditorInterface
/usr/include/qt5/QtDesigner/QDesignerComponents
/usr/include/qt5/QtDesigner/QDesignerContainerExtension
/usr/include/qt5/QtDesigner/QDesignerCustomWidgetCollectionInterface
/usr/include/qt5/QtDesigner/QDesignerCustomWidgetInterface
/usr/include/qt5/QtDesigner/QDesignerDnDItemInterface
/usr/include/qt5/QtDesigner/QDesignerDynamicPropertySheetExtension
/usr/include/qt5/QtDesigner/QDesignerExportWidget
/usr/include/qt5/QtDesigner/QDesignerExtraInfoExtension
/usr/include/qt5/QtDesigner/QDesignerFormEditorInterface
/usr/include/qt5/QtDesigner/QDesignerFormEditorPluginInterface
/usr/include/qt5/QtDesigner/QDesignerFormWindowCursorInterface
/usr/include/qt5/QtDesigner/QDesignerFormWindowInterface
/usr/include/qt5/QtDesigner/QDesignerFormWindowManagerInterface
/usr/include/qt5/QtDesigner/QDesignerFormWindowToolInterface
/usr/include/qt5/QtDesigner/QDesignerIntegration
/usr/include/qt5/QtDesigner/QDesignerIntegrationInterface
/usr/include/qt5/QtDesigner/QDesignerLanguageExtension
/usr/include/qt5/QtDesigner/QDesignerLayoutDecorationExtension
/usr/include/qt5/QtDesigner/QDesignerMemberSheetExtension
/usr/include/qt5/QtDesigner/QDesignerMetaDataBaseInterface
/usr/include/qt5/QtDesigner/QDesignerMetaDataBaseItemInterface
/usr/include/qt5/QtDesigner/QDesignerNewFormWidgetInterface
/usr/include/qt5/QtDesigner/QDesignerObjectInspectorInterface
/usr/include/qt5/QtDesigner/QDesignerOptionsPageInterface
/usr/include/qt5/QtDesigner/QDesignerPromotionInterface
/usr/include/qt5/QtDesigner/QDesignerPropertyEditorInterface
/usr/include/qt5/QtDesigner/QDesignerPropertySheetExtension
/usr/include/qt5/QtDesigner/QDesignerResourceBrowserInterface
/usr/include/qt5/QtDesigner/QDesignerSettingsInterface
/usr/include/qt5/QtDesigner/QDesignerTaskMenuExtension
/usr/include/qt5/QtDesigner/QDesignerWidgetBoxInterface
/usr/include/qt5/QtDesigner/QDesignerWidgetDataBaseInterface
/usr/include/qt5/QtDesigner/QDesignerWidgetDataBaseItemInterface
/usr/include/qt5/QtDesigner/QDesignerWidgetFactoryInterface
/usr/include/qt5/QtDesigner/QExtensionFactory
/usr/include/qt5/QtDesigner/QExtensionManager
/usr/include/qt5/QtDesigner/QFormBuilder
/usr/include/qt5/QtDesigner/QtDesigner
/usr/include/qt5/QtDesigner/QtDesignerDepends
/usr/include/qt5/QtDesigner/QtDesignerVersion
/usr/include/qt5/QtDesigner/abstractactioneditor.h
/usr/include/qt5/QtDesigner/abstractdnditem.h
/usr/include/qt5/QtDesigner/abstractformbuilder.h
/usr/include/qt5/QtDesigner/abstractformeditor.h
/usr/include/qt5/QtDesigner/abstractformeditorplugin.h
/usr/include/qt5/QtDesigner/abstractformwindow.h
/usr/include/qt5/QtDesigner/abstractformwindowcursor.h
/usr/include/qt5/QtDesigner/abstractformwindowmanager.h
/usr/include/qt5/QtDesigner/abstractformwindowtool.h
/usr/include/qt5/QtDesigner/abstractintegration.h
/usr/include/qt5/QtDesigner/abstractlanguage.h
/usr/include/qt5/QtDesigner/abstractmetadatabase.h
/usr/include/qt5/QtDesigner/abstractnewformwidget.h
/usr/include/qt5/QtDesigner/abstractobjectinspector.h
/usr/include/qt5/QtDesigner/abstractoptionspage.h
/usr/include/qt5/QtDesigner/abstractpromotioninterface.h
/usr/include/qt5/QtDesigner/abstractpropertyeditor.h
/usr/include/qt5/QtDesigner/abstractresourcebrowser.h
/usr/include/qt5/QtDesigner/abstractsettings.h
/usr/include/qt5/QtDesigner/abstractwidgetbox.h
/usr/include/qt5/QtDesigner/abstractwidgetdatabase.h
/usr/include/qt5/QtDesigner/abstractwidgetfactory.h
/usr/include/qt5/QtDesigner/container.h
/usr/include/qt5/QtDesigner/customwidget.h
/usr/include/qt5/QtDesigner/default_extensionfactory.h
/usr/include/qt5/QtDesigner/dynamicpropertysheet.h
/usr/include/qt5/QtDesigner/extension.h
/usr/include/qt5/QtDesigner/extension_global.h
/usr/include/qt5/QtDesigner/extrainfo.h
/usr/include/qt5/QtDesigner/formbuilder.h
/usr/include/qt5/QtDesigner/layoutdecoration.h
/usr/include/qt5/QtDesigner/membersheet.h
/usr/include/qt5/QtDesigner/propertysheet.h
/usr/include/qt5/QtDesigner/qdesigner_components.h
/usr/include/qt5/QtDesigner/qdesigner_components_global.h
/usr/include/qt5/QtDesigner/qdesignerexportwidget.h
/usr/include/qt5/QtDesigner/qextensionmanager.h
/usr/include/qt5/QtDesigner/qtdesignerversion.h
/usr/include/qt5/QtDesigner/sdk_global.h
/usr/include/qt5/QtDesigner/taskmenu.h
/usr/include/qt5/QtDesigner/uilib_global.h
/usr/include/qt5/QtDesignerComponents/5.10.1/QtDesignerComponents/private/lib_pch.h
/usr/include/qt5/QtDesignerComponents/QtDesignerComponents
/usr/include/qt5/QtDesignerComponents/QtDesignerComponentsDepends
/usr/include/qt5/QtDesignerComponents/QtDesignerComponentsVersion
/usr/include/qt5/QtDesignerComponents/qtdesignercomponentsversion.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpcollectionhandler_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpdatainterface_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpdbreader_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpengine_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpgenerator_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpprojectdata_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpsearchindexreader_default_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpsearchindexreader_p.h
/usr/include/qt5/QtHelp/5.10.1/QtHelp/private/qhelpsearchindexwriter_default_p.h
/usr/include/qt5/QtHelp/QHelpContentItem
/usr/include/qt5/QtHelp/QHelpContentModel
/usr/include/qt5/QtHelp/QHelpContentWidget
/usr/include/qt5/QtHelp/QHelpEngine
/usr/include/qt5/QtHelp/QHelpEngineCore
/usr/include/qt5/QtHelp/QHelpGlobal
/usr/include/qt5/QtHelp/QHelpIndexModel
/usr/include/qt5/QtHelp/QHelpIndexWidget
/usr/include/qt5/QtHelp/QHelpSearchEngine
/usr/include/qt5/QtHelp/QHelpSearchQuery
/usr/include/qt5/QtHelp/QHelpSearchQueryWidget
/usr/include/qt5/QtHelp/QHelpSearchResult
/usr/include/qt5/QtHelp/QHelpSearchResultWidget
/usr/include/qt5/QtHelp/QtHelp
/usr/include/qt5/QtHelp/QtHelpDepends
/usr/include/qt5/QtHelp/QtHelpVersion
/usr/include/qt5/QtHelp/qhelp_global.h
/usr/include/qt5/QtHelp/qhelpcontentwidget.h
/usr/include/qt5/QtHelp/qhelpengine.h
/usr/include/qt5/QtHelp/qhelpenginecore.h
/usr/include/qt5/QtHelp/qhelpindexwidget.h
/usr/include/qt5/QtHelp/qhelpsearchengine.h
/usr/include/qt5/QtHelp/qhelpsearchquerywidget.h
/usr/include/qt5/QtHelp/qhelpsearchresultwidget.h
/usr/include/qt5/QtHelp/qthelpversion.h
/usr/include/qt5/QtUiPlugin/QDesignerCustomWidgetCollectionInterface
/usr/include/qt5/QtUiPlugin/QDesignerCustomWidgetInterface
/usr/include/qt5/QtUiPlugin/QDesignerExportWidget
/usr/include/qt5/QtUiPlugin/QtUiPlugin
/usr/include/qt5/QtUiPlugin/QtUiPluginDepends
/usr/include/qt5/QtUiPlugin/QtUiPluginVersion
/usr/include/qt5/QtUiPlugin/customwidget.h
/usr/include/qt5/QtUiPlugin/qdesignerexportwidget.h
/usr/include/qt5/QtUiPlugin/qtuipluginversion.h
/usr/include/qt5/QtUiTools/5.10.1/QtUiTools/private/quiloader_p.h
/usr/include/qt5/QtUiTools/QUiLoader
/usr/include/qt5/QtUiTools/QtUiTools
/usr/include/qt5/QtUiTools/QtUiToolsDepends
/usr/include/qt5/QtUiTools/QtUiToolsVersion
/usr/include/qt5/QtUiTools/qtuitoolsversion.h
/usr/include/qt5/QtUiTools/quiloader.h
/usr/lib64/*.a
/usr/lib64/cmake/Qt5Designer/Qt5DesignerConfig.cmake
/usr/lib64/cmake/Qt5Designer/Qt5DesignerConfigVersion.cmake
/usr/lib64/cmake/Qt5Designer/Qt5Designer_QQuickWidgetPlugin.cmake
/usr/lib64/cmake/Qt5Help/Qt5HelpConfig.cmake
/usr/lib64/cmake/Qt5Help/Qt5HelpConfigExtras.cmake
/usr/lib64/cmake/Qt5Help/Qt5HelpConfigVersion.cmake
/usr/lib64/cmake/Qt5LinguistTools/Qt5LinguistToolsConfig.cmake
/usr/lib64/cmake/Qt5LinguistTools/Qt5LinguistToolsConfigVersion.cmake
/usr/lib64/cmake/Qt5LinguistTools/Qt5LinguistToolsMacros.cmake
/usr/lib64/cmake/Qt5UiPlugin/Qt5UiPluginConfig.cmake
/usr/lib64/cmake/Qt5UiPlugin/Qt5UiPluginConfigVersion.cmake
/usr/lib64/cmake/Qt5UiTools/Qt5UiToolsConfig.cmake
/usr/lib64/cmake/Qt5UiTools/Qt5UiToolsConfigVersion.cmake
/usr/lib64/libQt5Designer.la
/usr/lib64/libQt5Designer.prl
/usr/lib64/libQt5Designer.so
/usr/lib64/libQt5DesignerComponents.la
/usr/lib64/libQt5DesignerComponents.prl
/usr/lib64/libQt5DesignerComponents.so
/usr/lib64/libQt5Help.la
/usr/lib64/libQt5Help.prl
/usr/lib64/libQt5Help.so
/usr/lib64/libQt5UiTools.la
/usr/lib64/libQt5UiTools.prl
/usr/lib64/pkgconfig/Qt5Designer.pc
/usr/lib64/pkgconfig/Qt5Help.pc
/usr/lib64/pkgconfig/Qt5UiTools.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_designer.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_designer_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_help.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_help_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_uiplugin.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_uitools.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_uitools_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Designer.so.5
/usr/lib64/libQt5Designer.so.5.10
/usr/lib64/libQt5Designer.so.5.10.1
/usr/lib64/libQt5DesignerComponents.so.5
/usr/lib64/libQt5DesignerComponents.so.5.10
/usr/lib64/libQt5DesignerComponents.so.5.10.1
/usr/lib64/libQt5Help.so.5
/usr/lib64/libQt5Help.so.5.10
/usr/lib64/libQt5Help.so.5.10.1
/usr/lib64/qt5/plugins/designer/libqquickwidget.so
