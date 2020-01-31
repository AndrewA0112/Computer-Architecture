# Print out all of the strings in the following array in alphabetical order, each on a separate line:
words = ['PostScript', 'Moto', 'xBase', 'CFML', 'C Shell', 'Dart', 'PL/I', 'Gambas',
'WebDNA', 'IDL', 'Tex', 'Clojure', 'cT', 'Algol', 'S-PLUS', 'Transact-SQL',
'OPL', 'Eiffel', 'AppleScript', 'Google AppsScript', 'Yorick', 'EXEC',
'MAXScript', 'VBScript', 'bc', 'yacc', 'OpenEdge ABL', 'ASP', 'MANTIS',
'Puppet', 'AutoLISP', 'Limbo', 'Mirah', 'sed', 'PowerBasic', 'Informix-4GL',
'BlitzMax', 'LotusScript','(Visual) Basic', 'PL/SQL', 'Caml', 'Objective-C',
'GNU Octave', 'BCPL', 'Nu', 'Rust', 'Kotlin', 'Miva', 'Opa', 'Falcon',
'PowerShell', 'thinBasic', 'Whitespace', 'M4', 'SPSS', 'Malbolge', 'Prolog',
'Maple', 'EGL', 'Standard ML', 'Agilent VEE', 'VHDL', 'Tcl', 'Augeas', 'Fancy',
'Ada', 'Scilab', 'Parrot', 'X10', 'Heron', 'Gosu', 'C++', 'TACL', 'C','COMAL',
'Nimrod', 'Etoys', 'MOO', 'J#', 'APL', 'Curl', 'Seed7', 'Assembly',
'ActionScript', 'ooc','Q', 'XPL', 'REBOL', 'Simula', 'Fortran', 'D', 'J',
'Perl', 'Magik', 'TOM', 'Io', 'PHP', 'Pike', 'MEL', 'Monkey', 'Racket',
'Elixir', 'SuperCollider', 'Dylan', 'C#', 'XSLT', '(Visual) FoxPro', 'AutoIt',
'Lua', 'NXT-G', 'Processing', 'BETA', 'AspectJ', 'Paradox', 'REXX', 'C++/CLI',
'Ceylon', 'Arduino', 'MAD', 'CoffeeScript', 'Apex', 'Lisp', 'Pascal', 'Inform',
'HPL', 'Vala/Genie', 'Forth', 'Alice', 'Bourne Shell', 'DCPU-16 ASM', 'Xen',
'Magic', 'Logtalk', 'RPG (OS/400)', 'MATLAB', 'SPARK', 'Scheme', 'Groovy',
'Modula-3', 'ABC', '4th Dimension/4D', 'VimL', 'Bro', 'Squirrel', 'Lasso',
'JScript.NET', 'Smalltalk', 'Clipper', 'Awk', 'POV-Ray', 'Oberon', 'Emacs Lisp',
'XQuery', 'Ioke', 'ATLAS', 'Ecl', 'Oz', 'Scratch', 'SQR', 'REALBasic', 'NSIS',
'MUMPS', 'Shell', 'Bash', 'MS-DOS Batch', 'Self', 'OCaml', 'S', 'ABAP',
'Suneido', 'E', 'Fortress', 'Lingo', 'Ladder Logic', 'ColdFusion', 'JADE',
'JScript', 'CIL', 'Common Lisp', 'Icon', 'AutoHotkey', 'Python', 'Factor',
'Clarion', 'Objective-J', 'Delphi/Object Pascal', 'Simulink', 'Squeak', 'Felix',
'Visual Basic .NET', 'HyperTalk', 'DiBOL', 'LPC', 'Mercury', 'Object Rexx',
'Clean', 'SAS', 'SIGNAL', 'Z shell', 'Pliant', 'Java FX Script', 'CHILL',
'Logo', 'Ruby', 'COBOL', 'Ch', 'Slate', 'TypeScript', 'Java', 'OpenCL', 'Coq',
'INTERCAL', 'Boo','Turing', 'Avenue', 'Lustre', 'Modula-2', 'Arc', 'NATURAL',
'DCL', 'Korn Shell', 'Haskell', 'Max/MSP', 'eC', 'Go', 'Sather', 'Nemerle',
'haXe', 'ML','XBase++', 'Occam', 'F#', 'Pure Data', 'Angelscript',
'Mathematica', 'ECMAScript', 'PILOT', 'LabVIEW', 'Julia', 'Automator', 'Cobra',
'Scala', 'Revolution', 'Euphoria', 'CL (OS/400)', 'CLU', 'JavaScript', 'Smarty',
'C-Omega', 'cg', 'Fantom', 'PowerScript', 'Erlang', 'Verilog', 'NQC', 'R']
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
lower_words = []
for w in words:
    lower_words.append(w.lower())
lower_words.sort()
print(lower_words)