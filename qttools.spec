#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : qttools
Version  : 5.15.2
Release  : 38
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qttools-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qttools-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qttools-bin = %{version}-%{release}
Requires: qttools-data = %{version}-%{release}
Requires: qttools-lib = %{version}-%{release}
Requires: qttools-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : qtdeclarative-staticdev
Patch1: qttools-stable-branch.patch

%description
This tool allows introspection of incoming events for a QWidget, similar to the X11 xev tool.

%package bin
Summary: bin components for the qttools package.
Group: Binaries
Requires: qttools-data = %{version}-%{release}
Requires: qttools-license = %{version}-%{release}

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
Requires: qttools-lib = %{version}-%{release}
Requires: qttools-bin = %{version}-%{release}
Requires: qttools-data = %{version}-%{release}
Provides: qttools-devel = %{version}-%{release}
Requires: qttools = %{version}-%{release}

%description dev
dev components for the qttools package.


%package examples
Summary: examples components for the qttools package.
Group: Default
Requires: qttools-dev = %{version}-%{release}

%description examples
examples components for the qttools package.


%package lib
Summary: lib components for the qttools package.
Group: Libraries
Requires: qttools-data = %{version}-%{release}
Requires: qttools-license = %{version}-%{release}

%description lib
lib components for the qttools package.


%package license
Summary: license components for the qttools package.
Group: Default

%description license
license components for the qttools package.


%prep
%setup -q -n qttools-everywhere-src-5.15.2
cd %{_builddir}/qttools-everywhere-src-5.15.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1654786893
rm -rf %{buildroot}
## install_prepend content
pushd src/designer/src/uitools
make clean
qmake QMAKE_CXXFLAGS+=-fno-lto        # Can't have LTO (static)
make
popd
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/qttools
cp %{_builddir}/qttools-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qttools/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qttools-everywhere-src-5.15.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qttools/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qttools-everywhere-src-5.15.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qttools/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qttools-everywhere-src-5.15.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qttools/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qttools-everywhere-src-5.15.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qttools/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qttools-everywhere-src-5.15.2/tests/manual/qtattributionsscanner/data/LICENSE %{buildroot}/usr/share/package-licenses/qttools/673921c2954e5b10a7388e0a2fc6be083a609bd3
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_AnalogClockPlugin.cmake
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_MultiPageWidgetPlugin.cmake
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_TicTacToePlugin.cmake
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_WorldTimeClockPlugin.cmake
## install_append content
# Work around https://bugreports.qt.io/browse/QTBUG-78286
sed -i 's/lib"/lib64"/' %{buildroot}/usr/lib64/cmake/Qt5UiTools/*
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/assistant
/usr/bin/lprodump
/usr/bin/lrelease-pro
/usr/bin/lupdate-pro
/usr/bin/qcollectiongenerator
/usr/bin/qdbus
/usr/bin/qdbusviewer
/usr/bin/qtdiag
/usr/bin/qtpaths

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
/usr/bin/designer
/usr/bin/lconvert
/usr/bin/linguist
/usr/bin/lrelease
/usr/bin/lupdate
/usr/bin/pixeltool
/usr/bin/qdistancefieldgenerator
/usr/bin/qhelpgenerator
/usr/bin/qtattributionsscanner
/usr/bin/qtplugininfo
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/abstractdialoggui_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/abstractintrospection_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/actioneditor_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/actionprovider_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/actionrepository_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/codedialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/connectionedit_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/csshighlighter_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/deviceprofile_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/dialoggui_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/extensionfactory_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/formbuilderextra_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/formlayoutmenu_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/formwindowbase_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/grid_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/gridpanel_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/htmlhighlighter_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/iconloader_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/iconselector_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/invisible_widget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/layout_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/layoutinfo_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/lib_pch.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/metadatabase_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/morphmenu_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/newactiondialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/newformwidget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/orderdialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/plaintexteditor_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/plugindialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/pluginmanager_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/previewconfigurationwidget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/previewmanager_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/promotionmodel_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/promotiontaskmenu_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/properties_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/propertylineedit_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_command2_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_command_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_dnditem_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_dockwidget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_formbuilder_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_formeditorcommand_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_formwindowcommand_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_formwindowmanager_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_introspection_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_membersheet_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_menu_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_menubar_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_objectinspector_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_promotion_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_promotiondialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_propertycommand_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_propertyeditor_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_propertysheet_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_qsettings_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_stackedbox_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_tabwidget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_taskmenu_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_toolbar_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_toolbox_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_utils_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_widget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_widgetbox_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qdesigner_widgetitem_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qlayout_widget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qsimpleresource_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qtresourceeditordialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qtresourcemodel_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/qtresourceview_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/rcc_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/resourcebuilder_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/richtexteditor_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/selectsignaldialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/shared_enums_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/shared_global_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/shared_settings_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/sheet_delegate_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/signalslotdialog_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/spacer_widget_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/stylesheeteditor_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/textbuilder_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/textpropertyeditor_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/ui4_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/widgetdatabase_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/widgetfactory_p.h
/usr/include/qt5/QtDesigner/5.15.2/QtDesigner/private/zoomwidget_p.h
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
/usr/include/qt5/QtDesignerComponents/5.15.2/QtDesignerComponents/private/lib_pch.h
/usr/include/qt5/QtDesignerComponents/QtDesignerComponents
/usr/include/qt5/QtDesignerComponents/QtDesignerComponentsDepends
/usr/include/qt5/QtDesignerComponents/QtDesignerComponentsVersion
/usr/include/qt5/QtDesignerComponents/qtdesignercomponentsversion.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qfilternamedialog_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpcollectionhandler_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpdbreader_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpengine_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpfiltersettings_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpsearchindexreader_default_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpsearchindexreader_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qhelpsearchindexwriter_default_p.h
/usr/include/qt5/QtHelp/5.15.2/QtHelp/private/qoptionswidget_p.h
/usr/include/qt5/QtHelp/QCompressedHelpInfo
/usr/include/qt5/QtHelp/QHelpContentItem
/usr/include/qt5/QtHelp/QHelpContentModel
/usr/include/qt5/QtHelp/QHelpContentWidget
/usr/include/qt5/QtHelp/QHelpEngine
/usr/include/qt5/QtHelp/QHelpEngineCore
/usr/include/qt5/QtHelp/QHelpFilterData
/usr/include/qt5/QtHelp/QHelpFilterEngine
/usr/include/qt5/QtHelp/QHelpFilterSettingsWidget
/usr/include/qt5/QtHelp/QHelpGlobal
/usr/include/qt5/QtHelp/QHelpIndexModel
/usr/include/qt5/QtHelp/QHelpIndexWidget
/usr/include/qt5/QtHelp/QHelpLink
/usr/include/qt5/QtHelp/QHelpSearchEngine
/usr/include/qt5/QtHelp/QHelpSearchQuery
/usr/include/qt5/QtHelp/QHelpSearchQueryWidget
/usr/include/qt5/QtHelp/QHelpSearchResult
/usr/include/qt5/QtHelp/QHelpSearchResultWidget
/usr/include/qt5/QtHelp/QtHelp
/usr/include/qt5/QtHelp/QtHelpDepends
/usr/include/qt5/QtHelp/QtHelpVersion
/usr/include/qt5/QtHelp/qcompressedhelpinfo.h
/usr/include/qt5/QtHelp/qhelp_global.h
/usr/include/qt5/QtHelp/qhelpcontentwidget.h
/usr/include/qt5/QtHelp/qhelpengine.h
/usr/include/qt5/QtHelp/qhelpenginecore.h
/usr/include/qt5/QtHelp/qhelpfilterdata.h
/usr/include/qt5/QtHelp/qhelpfilterengine.h
/usr/include/qt5/QtHelp/qhelpfiltersettingswidget.h
/usr/include/qt5/QtHelp/qhelpindexwidget.h
/usr/include/qt5/QtHelp/qhelplink.h
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
/usr/include/qt5/QtUiTools/5.15.2/QtUiTools/private/quiloader_p.h
/usr/include/qt5/QtUiTools/QUiLoader
/usr/include/qt5/QtUiTools/QtUiTools
/usr/include/qt5/QtUiTools/QtUiToolsDepends
/usr/include/qt5/QtUiTools/QtUiToolsVersion
/usr/include/qt5/QtUiTools/qtuitoolsversion.h
/usr/include/qt5/QtUiTools/quiloader.h
/usr/lib64/cmake/Qt5AttributionsScannerTools/Qt5AttributionsScannerToolsConfig.cmake
/usr/lib64/cmake/Qt5AttributionsScannerTools/Qt5AttributionsScannerToolsConfigVersion.cmake
/usr/lib64/cmake/Qt5Designer/Qt5DesignerConfig.cmake
/usr/lib64/cmake/Qt5Designer/Qt5DesignerConfigVersion.cmake
/usr/lib64/cmake/Qt5Designer/Qt5Designer_QQuickWidgetPlugin.cmake
/usr/lib64/cmake/Qt5DesignerComponents/Qt5DesignerComponentsConfig.cmake
/usr/lib64/cmake/Qt5DesignerComponents/Qt5DesignerComponentsConfigVersion.cmake
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
/usr/lib64/libQt5Designer.prl
/usr/lib64/libQt5Designer.so
/usr/lib64/libQt5DesignerComponents.prl
/usr/lib64/libQt5DesignerComponents.so
/usr/lib64/libQt5Help.prl
/usr/lib64/libQt5Help.so
/usr/lib64/libQt5UiPlugin.prl
/usr/lib64/libQt5UiTools.a
/usr/lib64/libQt5UiTools.prl
/usr/lib64/pkgconfig/Qt5Designer.pc
/usr/lib64/pkgconfig/Qt5Help.pc
/usr/lib64/pkgconfig/Qt5UiPlugin.pc
/usr/lib64/pkgconfig/Qt5UiTools.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_designer.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_designer_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_help.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_help_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_uiplugin.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_uitools.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_uitools_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/assistant/assistant.pro
/usr/share/qt5/examples/assistant/remotecontrol/enter.png
/usr/share/qt5/examples/assistant/remotecontrol/main.cpp
/usr/share/qt5/examples/assistant/remotecontrol/remotecontrol.cpp
/usr/share/qt5/examples/assistant/remotecontrol/remotecontrol.h
/usr/share/qt5/examples/assistant/remotecontrol/remotecontrol.pro
/usr/share/qt5/examples/assistant/remotecontrol/remotecontrol.qrc
/usr/share/qt5/examples/assistant/remotecontrol/remotecontrol.ui
/usr/share/qt5/examples/assistant/simpletextviewer/assistant.cpp
/usr/share/qt5/examples/assistant/simpletextviewer/assistant.h
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/about.txt
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/browse.html
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/filedialog.html
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/findfile.html
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/browse.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/fadedfilemenu.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/filedialog.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/handbook.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/icon.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/mainwindow.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/open.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/images/wildcard.png
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/index.html
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/intro.html
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/openfile.html
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/simpletextviewer.qch
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/simpletextviewer.qhc
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/simpletextviewer.qhcp
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/simpletextviewer.qhp
/usr/share/qt5/examples/assistant/simpletextviewer/documentation/wildcardmatching.html
/usr/share/qt5/examples/assistant/simpletextviewer/findfiledialog.cpp
/usr/share/qt5/examples/assistant/simpletextviewer/findfiledialog.h
/usr/share/qt5/examples/assistant/simpletextviewer/main.cpp
/usr/share/qt5/examples/assistant/simpletextviewer/mainwindow.cpp
/usr/share/qt5/examples/assistant/simpletextviewer/mainwindow.h
/usr/share/qt5/examples/assistant/simpletextviewer/simpletextviewer.pro
/usr/share/qt5/examples/assistant/simpletextviewer/textedit.cpp
/usr/share/qt5/examples/assistant/simpletextviewer/textedit.h
/usr/share/qt5/examples/designer/README
/usr/share/qt5/examples/designer/calculatorbuilder/calculatorbuilder.pro
/usr/share/qt5/examples/designer/calculatorbuilder/calculatorbuilder.qrc
/usr/share/qt5/examples/designer/calculatorbuilder/calculatorform.cpp
/usr/share/qt5/examples/designer/calculatorbuilder/calculatorform.h
/usr/share/qt5/examples/designer/calculatorbuilder/calculatorform.ui
/usr/share/qt5/examples/designer/calculatorbuilder/main.cpp
/usr/share/qt5/examples/designer/calculatorform/calculatorform.cpp
/usr/share/qt5/examples/designer/calculatorform/calculatorform.h
/usr/share/qt5/examples/designer/calculatorform/calculatorform.pro
/usr/share/qt5/examples/designer/calculatorform/calculatorform.ui
/usr/share/qt5/examples/designer/calculatorform/main.cpp
/usr/share/qt5/examples/designer/containerextension/containerextension.pro
/usr/share/qt5/examples/designer/containerextension/multipagewidget.cpp
/usr/share/qt5/examples/designer/containerextension/multipagewidget.h
/usr/share/qt5/examples/designer/containerextension/multipagewidgetcontainerextension.cpp
/usr/share/qt5/examples/designer/containerextension/multipagewidgetcontainerextension.h
/usr/share/qt5/examples/designer/containerextension/multipagewidgetextensionfactory.cpp
/usr/share/qt5/examples/designer/containerextension/multipagewidgetextensionfactory.h
/usr/share/qt5/examples/designer/containerextension/multipagewidgetplugin.cpp
/usr/share/qt5/examples/designer/containerextension/multipagewidgetplugin.h
/usr/share/qt5/examples/designer/customwidgetplugin/analogclock.cpp
/usr/share/qt5/examples/designer/customwidgetplugin/analogclock.h
/usr/share/qt5/examples/designer/customwidgetplugin/customwidgetplugin.cpp
/usr/share/qt5/examples/designer/customwidgetplugin/customwidgetplugin.h
/usr/share/qt5/examples/designer/customwidgetplugin/customwidgetplugin.pro
/usr/share/qt5/examples/designer/designer.pro
/usr/share/qt5/examples/designer/taskmenuextension/taskmenuextension.pro
/usr/share/qt5/examples/designer/taskmenuextension/tictactoe.cpp
/usr/share/qt5/examples/designer/taskmenuextension/tictactoe.h
/usr/share/qt5/examples/designer/taskmenuextension/tictactoedialog.cpp
/usr/share/qt5/examples/designer/taskmenuextension/tictactoedialog.h
/usr/share/qt5/examples/designer/taskmenuextension/tictactoeplugin.cpp
/usr/share/qt5/examples/designer/taskmenuextension/tictactoeplugin.h
/usr/share/qt5/examples/designer/taskmenuextension/tictactoetaskmenu.cpp
/usr/share/qt5/examples/designer/taskmenuextension/tictactoetaskmenu.h
/usr/share/qt5/examples/designer/worldtimeclockbuilder/form.ui
/usr/share/qt5/examples/designer/worldtimeclockbuilder/main.cpp
/usr/share/qt5/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder.pro
/usr/share/qt5/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder.qrc
/usr/share/qt5/examples/designer/worldtimeclockplugin/worldtimeclock.cpp
/usr/share/qt5/examples/designer/worldtimeclockplugin/worldtimeclock.h
/usr/share/qt5/examples/designer/worldtimeclockplugin/worldtimeclockplugin.cpp
/usr/share/qt5/examples/designer/worldtimeclockplugin/worldtimeclockplugin.h
/usr/share/qt5/examples/designer/worldtimeclockplugin/worldtimeclockplugin.pro
/usr/share/qt5/examples/help/README
/usr/share/qt5/examples/help/contextsensitivehelp/contextsensitivehelp.pro
/usr/share/qt5/examples/help/contextsensitivehelp/docs/amount.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/filter.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/plants.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/rain.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/source.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/temperature.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/time.html
/usr/share/qt5/examples/help/contextsensitivehelp/docs/wateringmachine.qch
/usr/share/qt5/examples/help/contextsensitivehelp/docs/wateringmachine.qhc
/usr/share/qt5/examples/help/contextsensitivehelp/docs/wateringmachine.qhcp
/usr/share/qt5/examples/help/contextsensitivehelp/docs/wateringmachine.qhp
/usr/share/qt5/examples/help/contextsensitivehelp/helpbrowser.cpp
/usr/share/qt5/examples/help/contextsensitivehelp/helpbrowser.h
/usr/share/qt5/examples/help/contextsensitivehelp/main.cpp
/usr/share/qt5/examples/help/contextsensitivehelp/wateringconfigdialog.cpp
/usr/share/qt5/examples/help/contextsensitivehelp/wateringconfigdialog.h
/usr/share/qt5/examples/help/contextsensitivehelp/wateringconfigdialog.ui
/usr/share/qt5/examples/help/help.pro
/usr/share/qt5/examples/linguist/README
/usr/share/qt5/examples/linguist/arrowpad/arrowpad.cpp
/usr/share/qt5/examples/linguist/arrowpad/arrowpad.h
/usr/share/qt5/examples/linguist/arrowpad/arrowpad.pro
/usr/share/qt5/examples/linguist/arrowpad/main.cpp
/usr/share/qt5/examples/linguist/arrowpad/mainwindow.cpp
/usr/share/qt5/examples/linguist/arrowpad/mainwindow.h
/usr/share/qt5/examples/linguist/hellotr/hellotr.pro
/usr/share/qt5/examples/linguist/hellotr/main.cpp
/usr/share/qt5/examples/linguist/linguist.pro
/usr/share/qt5/examples/linguist/trollprint/main.cpp
/usr/share/qt5/examples/linguist/trollprint/mainwindow.cpp
/usr/share/qt5/examples/linguist/trollprint/mainwindow.h
/usr/share/qt5/examples/linguist/trollprint/printpanel.cpp
/usr/share/qt5/examples/linguist/trollprint/printpanel.h
/usr/share/qt5/examples/linguist/trollprint/trollprint.pro
/usr/share/qt5/examples/linguist/trollprint/trollprint_pt.ts
/usr/share/qt5/examples/uitools/multipleinheritance/calculatorform.cpp
/usr/share/qt5/examples/uitools/multipleinheritance/calculatorform.h
/usr/share/qt5/examples/uitools/multipleinheritance/calculatorform.ui
/usr/share/qt5/examples/uitools/multipleinheritance/main.cpp
/usr/share/qt5/examples/uitools/multipleinheritance/multipleinheritance.pro
/usr/share/qt5/examples/uitools/textfinder/forms/input.txt
/usr/share/qt5/examples/uitools/textfinder/forms/textfinder.ui
/usr/share/qt5/examples/uitools/textfinder/main.cpp
/usr/share/qt5/examples/uitools/textfinder/textfinder.cpp
/usr/share/qt5/examples/uitools/textfinder/textfinder.h
/usr/share/qt5/examples/uitools/textfinder/textfinder.pro
/usr/share/qt5/examples/uitools/textfinder/textfinder.qrc
/usr/share/qt5/examples/uitools/uitools.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Designer.so.5
/usr/lib64/libQt5Designer.so.5.15
/usr/lib64/libQt5Designer.so.5.15.2
/usr/lib64/libQt5DesignerComponents.so.5
/usr/lib64/libQt5DesignerComponents.so.5.15
/usr/lib64/libQt5DesignerComponents.so.5.15.2
/usr/lib64/libQt5Help.so.5
/usr/lib64/libQt5Help.so.5.15
/usr/lib64/libQt5Help.so.5.15.2
/usr/lib64/qt5/plugins/designer/libqquickwidget.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qttools/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qttools/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qttools/673921c2954e5b10a7388e0a2fc6be083a609bd3
/usr/share/package-licenses/qttools/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qttools/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qttools/f45ee1c765646813b442ca58de72e20a64a7ddba
