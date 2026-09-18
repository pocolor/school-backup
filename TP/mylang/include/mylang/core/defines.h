#pragma once

#if defined(_WIN32)
#define MYLANG_OS_WIN
#error "Windows is not supported!"
#elif defined(__APPLE__) && defined(__MACH__)
#define MYLANG_OS_MACOS
#elif defined(__linux__)
#define MYLANG_OS_LINUX
#else
#error "Unknown os!"
#endif
