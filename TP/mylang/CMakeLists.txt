cmake_minimum_required(VERSION 4.0)
project(mylang LANGUAGES C)

set(MYLANG_BUILD_IS_DEBUG $<CONFIG:Debug>)
set(MYLANG_BUILD_IS_NDEBUG $<NOT:${MYLANG_BUILD_IS_DEBUG}>)

file(GLOB_RECURSE mylang_source ./src/*.c)
add_executable(mylang ${mylang_source})

target_compile_features(mylang PRIVATE c_std_23)

target_include_directories(mylang PUBLIC ./include)
target_include_directories(mylang PRIVATE ./src)

target_compile_definitions(mylang PUBLIC
        $<${MYLANG_BUILD_IS_DEBUG}:MYLANG_BUILD_DEBUG>
        $<${MYLANG_BUILD_IS_NDEBUG}:MYLANG_BUILD_NDEBUG>
)
