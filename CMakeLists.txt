cmake_minimum_required(VERSION 2.6)
project("IrrAssimp")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(ROOT_PATH ${CMAKE_SOURCE_DIR}/source_subfolder/IrrAssimp)

file(GLOB SOURCES
    ${ROOT_PATH}/*.hpp
    ${ROOT_PATH}/*.h
    ${ROOT_PATH}/*.cpp
    ${ROOT_PATH}/*.c
)

add_library(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} PRIVATE ${CONAN_LIBS})