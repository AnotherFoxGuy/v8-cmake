import os
from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import collect_libs

# conan create . --user overte --channel stable -c tools.cmake.cmaketoolchain:generator=Ninja

class V8Recipe(ConanFile):
    name = "v8"
    version = "10.2"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "v8/*", "cmake/*"

    def validate(self):
        check_min_cppstd(self, 17)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join("include", "v8"))
        self.cpp_info.libs = collect_libs(self)