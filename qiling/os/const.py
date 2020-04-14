#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

QL_ARCHBIT32_EMU_END = 0x8fffffff
QL_ARCHBIT64_EMU_END = 0xffffffffffffffff

#OS Threading Constants
THREAD_EVENT_INIT_VAL = 0
THREAD_EVENT_EXIT_EVENT = 1
THREAD_EVENT_UNEXECPT_EVENT = 2
THREAD_EVENT_EXECVE_EVENT = 3
THREAD_EVENT_CREATE_THREAD = 4
THREAD_EVENT_BLOCKING_EVENT = 5
THREAD_EVENT_EXIT_GROUP_EVENT = 6

THREAD_STATUS_RUNNING = 0
THREAD_STATUS_BLOCKING = 1
THREAD_STATUS_TERMINATED = 2
THREAD_STATUS_TIMEOUT = 3