import pyb

PinMapperDict = {
    'PB0' : pyb.Pin.cpu.B0,
    'PB7' : pyb.Pin.cpu.B7,
    'PB14' : pyb.Pin.cpu.B14,
    'LD1_GREEN' : pyb.Pin.cpu.B0,
    'LD2_BLUE' : pyb.Pin.cpu.B7,
    'LD3_RED' : pyb.Pin.cpu.B14,
    'PA3' : pyb.Pin.cpu.A3, # A0
    'PA6' : pyb.Pin.cpu.A6, # D12
    'PA4' : pyb.Pin.cpu.A4, # D24
    'PA5' : pyb.Pin.cpu.A5  # D13
}

pyb.Pin.dict(PinMapperDict)