from conans import ConanFile, CMake, tools
import os


class IrrAssimpConan(ConanFile):
    name = "IrrAssimp"
    version = "1.8.4"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    options = {
        "shared": [True, False]
    }

    default_options = {
        "shared": False
    }

    _source_subfolder = "source_subfolder"

    requires = [
        "irrlicht/1.8.4@mpusz/testing",     # https://api.bintray.com/conan/mpusz/conan-mpusz
        "assimp/5.0.1",                     # https://api.bintray.com/conan/bincrafters/public-conan
    ]

    @property
    def exports_sources(self):
        return [
            "CMakeLists.txt"
        ]

    def source(self):
        self.run("git clone --depth 1 https://github.com/JLouis-B/IrrAssimp.git %s" % self._source_subfolder)
        with tools.chdir(self._source_subfolder):
            self.run("git checkout aed2cab5505f0164689c2aebdb8d9f6c729066e6")  # Use fixed commit

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        if self.settings.os != "Linux":
            raise Exception("Not implemented (%s)" % os.name)

        self.copy("*.a", src="lib", dst="lib")
        self.copy("*.so", src="lib", dst="lib")
        self.copy("*.h", src="%s/IrrAssimp" % self._source_subfolder, dst="include/IrrAssimp")

    def package_info(self):
        self.cpp_info.libs = ["IrrAssimp"]
