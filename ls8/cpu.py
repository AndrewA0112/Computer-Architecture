"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * (2**8)
        self.pc = 0
        self.register = [0] * 8
        self.register[7] = 0xFF

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
        #elif op == "SUB": etc
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

            if ir == 0b00000001: # Halt
                running = False
                self.pc += 1

            elif ir == 0b01000111: # Print
                print(self.register[operand_a])
                self.pc += 2

            elif ir == 0b10000010: # Set register value
                self.register[operand_a] = operand_b
                self.pc += 3

            elif ir == 0b10100010: # Multiply registers
                result = self.register[operand_a] * self.register[operand_b]
                self.register[operand_a] = result
                self.pc += 3

            elif ir == 0b01000101: # Push register value to stack
                self.register[7] -= 1
                self.ram[self.register[7]] = self.register[operand_a]
                self.pc += 2

            elif ir == 0b01000110: # Pop register value from stack
                self.register[operand_a] = self.ram[self.register[7]]
                self.register[7] -= 1
                self.pc += 2

            else:
                print(f'Unknown instruction: {ir}')
                sys.exit(1)

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value