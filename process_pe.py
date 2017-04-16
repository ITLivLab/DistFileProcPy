def procpe(pe_file):
    import pefile
    pe = pefile.PE(pe_file)
    if pe.is_exe():
        pe_out = open(pe_file.split("/")[3]+".results","w")
        pe_out.write("Entry point: " + str(pe.OPTIONAL_HEADER.AddressOfEntryPoint)+"\n")
        pe_out.write("Number of Sections : " + str(pe.FILE_HEADER.NumberOfSections) + "\n")
        pe_out.write("Section names: \n")
        for section in pe.sections:
            pe_out.write(section.Name + "\n")
        pe_out.close()
        pe.close()
        return True
    else:
        return False
