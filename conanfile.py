from conans import ConanFile
from conans import tools

class TerseStlAlgorithmsConan(ConanFile):
    name = 'terse-stl-algorithms'
    url = 'https://github.com/owbone/conan-terse-stl-algorithms.git'
    tag = '79db5297539266ee97120997b4a5e075a602763f'
    git_repo = 'https://github.com/kberezovsky/Terse-STL-algorithms.git'
    version = tag[0:7]
    source_dir = 'terse-{}'.format(tag)

    def source(self):
        self.run('git clone {} {}'.format(self.git_repo, self.source_dir))
        self.run('cd {} && git checkout {}'.format(self.source_dir, self.tag))

    def build(self):
        # Header only.
        pass

    def package(self):
        self.copy(
            pattern='*',
            dst='include/terse',
            src='{}/terse'.format(self.source_dir)
        )
