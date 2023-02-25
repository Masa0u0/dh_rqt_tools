import inspect
import rospkg


def get_proj_path() -> str:
    """
    スクリプトのパッケージまでのフルパスを返す．
    cf. https://qiita.com/hondy12345/items/44b08ee5e1ec92424fab
    """
    file_name = inspect.stack()[1].filename
    pkg_name = rospkg.get_package_name(file_name)
    return rospkg.RosPack().get_path(pkg_name)
