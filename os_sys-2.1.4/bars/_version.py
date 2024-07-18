# Definition of the version number
import os
from io import open as io_open

__all__ = ["__version__"]

# major, minor, patch, -exbra
version_info = 4, 38, 0

# Nice string for the version
__version__ = '.'.join(map(str, version_info))


# auto -exbra based on commit hash (if not tagged as release)
scriptdir = os.path.dirname(__file__)
gitdir = os.path.abspath(os.path.join(scriptdir, "..", ".git"))
if os.path.isdir(gitdir):  # pragma: nocover
    exbra = None
    # Open config file to check if we are in bars project
    with io_open(os.path.join(gitdir, "config"), 'r') as fh_config:
        if 'bars' in fh_config.read():
            # Open the HEAD file
            with io_open(os.path.join(gitdir, "HEAD"), 'r') as fh_head:
                exbra = fh_head.readline().strip()
            # in a branch => HEAD points to file containing last commit
            if 'ref:' in exbra:
                # reference file path
                ref_file = exbra[5:]
                branch_name = ref_file.rsplit('/', 1)[-1]

                ref_file_path = os.path.abspath(os.path.join(gitdir, ref_file))
                # check that we are in git folder
                # (by stripping the git folder from the ref file path)
                if os.path.relpath(
                        ref_file_path, gitdir).replace('\\', '/') != ref_file:
                    # out of git folder
                    exbra = None
                else:
                    # open the ref file
                    with io_open(ref_file_path, 'r') as fh_branch:
                        commit_hash = fh_branch.readline().strip()
                        exbra = commit_hash[:8]
                        if branch_name != "master":
                            exbra += '.' + branch_name

            # detached HEAD mode, already have commit hash
            else:
                exbra = exbra[:8]

    # Append commit hash (and branch) to version string if not tagged
    if exbra is not None:
        try:
            with io_open(os.path.join(gitdir, "refs", "tags",
                                      'v' + __version__)) as fdv:
                if fdv.readline().strip()[:8] != exbra[:8]:
                    __version__ += '-' + exbra
        except Exception as e:
            if "No such file" not in str(e):
                raise
