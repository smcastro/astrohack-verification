import pytest

def test_import_astrohack_client():
    try:
        from astrohack.astrohack_client import astrohack_local_client
    except ImportError:
        assert False

def test_import_astrohack_holog():
    try:
        from astrohack.astrohack_holog import astrohack_holog
    except ImportError:
        assert False

def test_import_holog():
    try:
        from astrohack.holog import holog
    except ImportError:
        assert False

def test_import_panel():
    try:
        from astrohack.panel import panel
    except ImportError:
        assert False

def test_import_dio_open_holog():
    try:
        from astrohack.dio import open_holog
    except ImportError:
        assert False

def test_import_dio_open_image():
    try:
        from astrohack.dio import open_image
    except ImportError:
        assert False

def test_import_dio_open_panel():
    try:
        from astrohack.dio import open_panel
    except ImportError:
        assert False
 
def test_import_dio_open_pointing():
    try:
        from astrohack.dio import open_pointing
    except ImportError:
        assert False

def test_import_dio_fix_pointing_table():
    try:
        from astrohack.dio import fix_pointing_table
    except ImportError:
        assert False
        
def test_import_dio_export_screws():
    try:
        from astrohack.dio import export_screws
    except ImportError:
        assert False
        
def test_import_dio_plot_antenna():
    try:
        from astrohack.dio import plot_antenna
    except ImportError:
        assert False
        
def test_import_dio_export_to_fits():
    try:
        from astrohack.dio import export_to_fits
    except ImportError:
        assert False
        
        
