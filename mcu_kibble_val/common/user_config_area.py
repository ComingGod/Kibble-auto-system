#! /usr/bin/env python

# Copyright (c) 2014 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os

# @breif Constants
kInvalidValue32bits = 0xFFFFFFFF
kInvalidValue16bits = 0xFFFF
kInvalidValue8bits = 0xFF

# @breif Generate the BCA tag.
def four_char_code(a, b, c, d):
    return ((ord(d) << 24) | (ord(c) << 16) | (ord(b) << 8) | (ord(a)))

# @breif Fill the specific 8-bit data to bytearray.
def fill_data_8bits(byteArray, data8bits):
    byteArray.append(data8bits)
    return byteArray

# @breif Fill the specific 16-bit data to bytearray.
def fill_data_16bits(byteArray, data16bits):
    byteArray.append(data16bits & 0x00FF)
    byteArray.append((data16bits & 0xFF00) >> 8)
    return byteArray

# @breif Fill the specific 32-bit data to bytearray.
def fill_data_32bits(byteArray, data32bits):
    byteArray.append((data32bits & 0x000000FF))
    byteArray.append((data32bits & 0x0000FF00) >> 8)
    byteArray.append((data32bits & 0x00FF0000) >> 16)
    byteArray.append((data32bits & 0xFF000000) >> 24)
    return byteArray

# @breif Generate the BCA data.
def create_BCA_data_file(
                       bl,
                       tag                          =   four_char_code('k', 'c', 'f', 'g'),
                       crcStartAddress              =   kInvalidValue32bits,
                       crcByteCount                 =   kInvalidValue32bits,
                       crcExpectedValue             =   kInvalidValue32bits,
                       enabledPeripherals           =   kInvalidValue8bits,
                       i2cSlaveAddress              =   kInvalidValue8bits,
                       peripheralDetectionTimeout   =   kInvalidValue16bits,
                       usbVid                       =   kInvalidValue16bits,
                       usbPid                       =   kInvalidValue16bits,
                       usbStringsPointer            =   kInvalidValue32bits,
                       clockFlags                   =   kInvalidValue8bits,
                       clockDivider                 =   kInvalidValue8bits,
                       bootFlags                    =   kInvalidValue8bits,
                       pad0                         =   kInvalidValue8bits,
                       mmcauConfigPointer           =   kInvalidValue32bits,
                       keyBlobPointer               =   kInvalidValue32bits,
                       pad1                         =   kInvalidValue8bits,
                       canConfig1                   =   kInvalidValue8bits,
                       canConfig2                   =   kInvalidValue16bits,
                       canTxId                      =   kInvalidValue16bits,
                       canRxId                      =   kInvalidValue16bits,
                       qspiConfigBlockPointer       =   kInvalidValue32bits
                    ):
    bcaData = bytearray()
    # Fill the specific data to the BCA data array.
    fill_data_32bits(bcaData, tag)
    fill_data_32bits(bcaData, crcStartAddress)
    fill_data_32bits(bcaData, crcByteCount)
    fill_data_32bits(bcaData, crcExpectedValue)
    fill_data_8bits(bcaData, enabledPeripherals)
    fill_data_8bits(bcaData, i2cSlaveAddress)
    fill_data_16bits(bcaData, peripheralDetectionTimeout)
    fill_data_16bits(bcaData, usbVid)
    fill_data_16bits(bcaData, usbPid)
    fill_data_32bits(bcaData, usbStringsPointer)
    fill_data_8bits(bcaData, clockFlags)
    fill_data_8bits(bcaData, clockDivider)
    fill_data_8bits(bcaData, bootFlags)
    fill_data_8bits(bcaData, pad0)
    fill_data_32bits(bcaData, mmcauConfigPointer)
    fill_data_32bits(bcaData, keyBlobPointer)
    fill_data_8bits(bcaData, pad1)
    fill_data_8bits(bcaData, canConfig1)
    fill_data_16bits(bcaData, canConfig2)
    fill_data_16bits(bcaData, canTxId)
    fill_data_16bits(bcaData, canRxId)
    fill_data_32bits(bcaData, qspiConfigBlockPointer)

    # Write the BCA data bytes to the BCA.dat file
    bcaFilePath = os.path.join(bl.vectorsDir, 'BCA.dat')
    fileObj = open(bcaFilePath, 'w+')
    fileObj.write(bcaData)
    fileObj.close()
    return bcaFilePath

