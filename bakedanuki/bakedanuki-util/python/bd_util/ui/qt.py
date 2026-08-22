# coding: utf-8
"""Maya同梱Qt bindingのimport差分を吸収する。"""

from importlib import import_module
from types import ModuleType
from typing import TYPE_CHECKING, NamedTuple

# 新しいbindingを優先し、存在しない場合だけ次の候補へ切り替える。
_BINDING_CANDIDATES = (
    ("PySide7", "shiboken7"),
    ("PySide6", "shiboken6"),
)


class _BindingModules(NamedTuple):
    """1組のQt binding moduleを保持する。"""

    name: str
    binding: ModuleType
    qt_core: ModuleType
    qt_gui: ModuleType
    qt_widgets: ModuleType
    shiboken: ModuleType


def _load_binding(
    candidates: tuple[tuple[str, str], ...] = _BINDING_CANDIDATES,
) -> _BindingModules:
    """利用可能なQt bindingと対応するshibokenを読み込む。"""
    # 候補のroot packageだけを確認し、存在しない場合は次へ進む。
    for binding_name, shiboken_name in candidates:
        try:
            binding = import_module(binding_name)
        except ModuleNotFoundError as error:
            if error.name == binding_name:
                continue
            raise

        # 発見したbindingの内部import errorは隠さず、そのまま呼び出し元へ伝える。
        qt_core = import_module(f"{binding_name}.QtCore")
        qt_gui = import_module(f"{binding_name}.QtGui")
        qt_widgets = import_module(f"{binding_name}.QtWidgets")
        shiboken = import_module(shiboken_name)
        return _BindingModules(
            name=binding_name,
            binding=binding,
            qt_core=qt_core,
            qt_gui=qt_gui,
            qt_widgets=qt_widgets,
            shiboken=shiboken,
        )

    # 対応候補がない環境では、確認したbinding名を含む明確なerrorを送出する。
    candidate_names = ", ".join(name for name, _shiboken in candidates)
    raise ImportError(f"対応するQt bindingが見つかりません: {candidate_names}")


if TYPE_CHECKING:
    # 現在の基準bindingを静的importし、IDEの補完と型情報を維持する。
    import PySide6 as _binding
    from PySide6 import QtCore, QtGui, QtWidgets
    from shiboken6 import getCppPointer, isValid, wrapInstance

    QT_BINDING = "PySide6"
else:
    # 実行環境で選択したmoduleとshiboken helperを公開名へ割り当てる。
    _modules = _load_binding()
    QT_BINDING = _modules.name
    _binding = _modules.binding
    QtCore = _modules.qt_core
    QtGui = _modules.qt_gui
    QtWidgets = _modules.qt_widgets
    getCppPointer = _modules.shiboken.getCppPointer
    isValid = _modules.shiboken.isValid
    wrapInstance = _modules.shiboken.wrapInstance

# 利用中のbinding情報を診断やversion分岐で参照できるよう公開する。
QT_BINDING_VERSION = _binding.__version__
QT_BINDING_MAJOR_VERSION = int(QT_BINDING.removeprefix("PySide"))

# Signal定義やenumで頻繁に使うQtCore APIを短い名前で公開する。
Qt = QtCore.Qt
Signal = QtCore.Signal
Slot = QtCore.Slot
Property = QtCore.Property
QObject = QtCore.QObject
QEvent = QtCore.QEvent
QTimer = QtCore.QTimer
QSettings = QtCore.QSettings
QByteArray = QtCore.QByteArray
QModelIndex = QtCore.QModelIndex
QAbstractItemModel = QtCore.QAbstractItemModel
QAbstractListModel = QtCore.QAbstractListModel
QSortFilterProxyModel = QtCore.QSortFilterProxyModel
QItemSelectionModel = QtCore.QItemSelectionModel
QPoint = QtCore.QPoint
QPointF = QtCore.QPointF
QSize = QtCore.QSize
QRect = QtCore.QRect
QUrl = QtCore.QUrl

# Icon、描画、event、item modelで頻繁に使うQtGui APIを公開する。
QAction = QtGui.QAction
QActionGroup = QtGui.QActionGroup
QCloseEvent = QtGui.QCloseEvent
QColor = QtGui.QColor
QCursor = QtGui.QCursor
QFont = QtGui.QFont
QIcon = QtGui.QIcon
QImage = QtGui.QImage
QKeySequence = QtGui.QKeySequence
QPainter = QtGui.QPainter
QPalette = QtGui.QPalette
QPixmap = QtGui.QPixmap
QStandardItem = QtGui.QStandardItem
QStandardItemModel = QtGui.QStandardItemModel
QValidator = QtGui.QValidator

# Window、layout、入力Widgetなど一般的なQtWidgets APIを公開する。
QApplication = QtWidgets.QApplication
QWidget = QtWidgets.QWidget
QDialog = QtWidgets.QDialog
QMainWindow = QtWidgets.QMainWindow
QDockWidget = QtWidgets.QDockWidget
QFrame = QtWidgets.QFrame
QLabel = QtWidgets.QLabel
QPushButton = QtWidgets.QPushButton
QToolButton = QtWidgets.QToolButton
QCheckBox = QtWidgets.QCheckBox
QRadioButton = QtWidgets.QRadioButton
QLineEdit = QtWidgets.QLineEdit
QTextEdit = QtWidgets.QTextEdit
QPlainTextEdit = QtWidgets.QPlainTextEdit
QComboBox = QtWidgets.QComboBox
QSpinBox = QtWidgets.QSpinBox
QDoubleSpinBox = QtWidgets.QDoubleSpinBox
QSlider = QtWidgets.QSlider
QProgressBar = QtWidgets.QProgressBar
QTabWidget = QtWidgets.QTabWidget
QStackedWidget = QtWidgets.QStackedWidget
QSplitter = QtWidgets.QSplitter
QScrollArea = QtWidgets.QScrollArea
QListView = QtWidgets.QListView
QListWidget = QtWidgets.QListWidget
QListWidgetItem = QtWidgets.QListWidgetItem
QTreeView = QtWidgets.QTreeView
QTreeWidget = QtWidgets.QTreeWidget
QTreeWidgetItem = QtWidgets.QTreeWidgetItem
QTableView = QtWidgets.QTableView
QTableWidget = QtWidgets.QTableWidget
QTableWidgetItem = QtWidgets.QTableWidgetItem
QHeaderView = QtWidgets.QHeaderView
QVBoxLayout = QtWidgets.QVBoxLayout
QHBoxLayout = QtWidgets.QHBoxLayout
QGridLayout = QtWidgets.QGridLayout
QFormLayout = QtWidgets.QFormLayout
QBoxLayout = QtWidgets.QBoxLayout
QStackedLayout = QtWidgets.QStackedLayout
QMenu = QtWidgets.QMenu
QMenuBar = QtWidgets.QMenuBar
QToolBar = QtWidgets.QToolBar
QStatusBar = QtWidgets.QStatusBar
QFileDialog = QtWidgets.QFileDialog
QMessageBox = QtWidgets.QMessageBox
QDialogButtonBox = QtWidgets.QDialogButtonBox
QGroupBox = QtWidgets.QGroupBox
QSizePolicy = QtWidgets.QSizePolicy
QSpacerItem = QtWidgets.QSpacerItem
QAbstractItemView = QtWidgets.QAbstractItemView
QStyledItemDelegate = QtWidgets.QStyledItemDelegate

__all__ = [
    "getCppPointer",
    "isValid",
    "Property",
    "QAbstractItemModel",
    "QAbstractItemView",
    "QAbstractListModel",
    "QAction",
    "QActionGroup",
    "QApplication",
    "QBoxLayout",
    "QByteArray",
    "QCheckBox",
    "QCloseEvent",
    "QColor",
    "QComboBox",
    "QCursor",
    "QDialog",
    "QDialogButtonBox",
    "QDockWidget",
    "QDoubleSpinBox",
    "QEvent",
    "QFileDialog",
    "QFont",
    "QFormLayout",
    "QFrame",
    "QGridLayout",
    "QGroupBox",
    "QHBoxLayout",
    "QHeaderView",
    "QIcon",
    "QImage",
    "QItemSelectionModel",
    "QKeySequence",
    "QLabel",
    "QLineEdit",
    "QListView",
    "QListWidget",
    "QListWidgetItem",
    "QMainWindow",
    "QMenu",
    "QMenuBar",
    "QMessageBox",
    "QModelIndex",
    "QObject",
    "QPainter",
    "QPalette",
    "QPixmap",
    "QPlainTextEdit",
    "QPoint",
    "QPointF",
    "QProgressBar",
    "QPushButton",
    "QRadioButton",
    "QRect",
    "QScrollArea",
    "QSettings",
    "QSize",
    "QSizePolicy",
    "QSlider",
    "QSortFilterProxyModel",
    "QSpacerItem",
    "QSpinBox",
    "QSplitter",
    "QStackedLayout",
    "QStackedWidget",
    "QStandardItem",
    "QStandardItemModel",
    "QStatusBar",
    "QStyledItemDelegate",
    "QTableView",
    "QTableWidget",
    "QTableWidgetItem",
    "QTabWidget",
    "QTextEdit",
    "QTimer",
    "QToolBar",
    "QToolButton",
    "QTreeView",
    "QTreeWidget",
    "QTreeWidgetItem",
    "Qt",
    "QtCore",
    "QtGui",
    "QtWidgets",
    "QT_BINDING",
    "QT_BINDING_MAJOR_VERSION",
    "QT_BINDING_VERSION",
    "QUrl",
    "QValidator",
    "QVBoxLayout",
    "QWidget",
    "Signal",
    "Slot",
    "wrapInstance",
]
