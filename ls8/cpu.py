"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
ADD = 0b10100000
POP = 0b01000110
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110
PUSH = 0b01000101
CALL = 0b01010000
RET = 0b00010001

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.register = [0] * 8
        self.register[7] = 0xFF
        self.fl = [0] * 8

    def load(self, file_name):
        """Load a program into memory."""
        address = 0

        with open('examples/' + file_name, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('\n'):
                    continue
                else:
                    cmd = line.split(' ')[0]
                    self.ram[address] = int(cmd, 2)
                    address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]

        elif op == "CMP":
            self.fl[5] = 0
            self.fl[6] = 0
            self.fl[7] = 0

            if self.register[reg_a] == self.register[reg_b]:
                self.fl[7] = 1
            elif self.register[reg_a] > self.register[reg_b]:
                self.fl[6] = 1
            elif self.register[reg_a] < self.register[reg_b]:
                self.fl[5] = 1

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.register[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        while running:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if ir == HLT:
                running = False
                self.pc += 1

            elif ir == PRN:
                print(self.register[operand_a])
                self.pc += 2  

            elif ir == LDI:
                self.register[operand_a] = operand_b
                self.pc += 3

            elif ir == MUL:
                result = self.register[operand_a] * self.register[operand_b]
                self.register[operand_a] = result
                self.pc += 3
            
            elif ir == ADD:
                result = self.register[operand_a] + self.register[operand_b]
                self.register[operand_a] = result
                self.pc += 3

            elif ir == PUSH:
                self.register[7] -= 1
                self.ram[self.register[7]] = self.register[operand_a]
                self.pc += 2

            elif ir == POP:
                self.register[operand_a] = self.ram[self.register[7]]
                self.register[7] += 1
                self.pc += 2

            elif ir == CALL:
                ret_address = self.pc + 2
                self.register[7] -= 1
                self.ram[self.register[7]] = ret_address

                self.pc = self.register[operand_a]
            
            elif ir == RET:
                self.pc = self.ram[self.register[7]]
                self.register[7] += 1
            
            elif ir == CMP:
                self.alu('CMP', operand_a, operand_b)
                self.pc += 3
            
            elif ir == JMP:
                self.pc = self.register[operand_a]
            
            elif ir == JEQ:
                if self.fl[7] == 1:
                    self.pc = self.register[operand_a]
                else:
                    self.pc += 2

            elif ir == JNE:
                if self.fl[7] == 0:
                    self.pc = self.register[operand_a]
                else:
                    self.pc += 2

            else:
                print(f'Unknown instruction: {ir} {self.pc}')
                sys.exit(1)

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value