import cmd
import xml.etree.ElementTree as ET
import fileopener as fo

appversion = "RESXVSV Version 0.1 201610051055\n"

class TagTerminal(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""

    prompt = "> "

    def do_convert(self, line):
        '''Type convert and the filename of the RESX file.'''

        try:
            can = fo.fileopener()
            xmlData = can.open(line)
            filestem = line[0:-5]
            filename = filestem + ".csv"
            xmldoc = ET.fromstring(xmlData)
            ns = {'xsd':'http://www.w3.org/2001/XMLSchema'}
            outfile = ("name, value\n")
            for d in xmldoc.findall('data',ns):
                outname = d.attrib["name"]
                for c in d:
                    if c.tag == "value":
                        outvalue = c.text
                        if outvalue == None:
                            outvalue = " "
                outfile = outfile + (d.attrib["name"]+", "+outvalue+"\n")
            f = open(filename,'w')
            for l in outfile:
                f.write(l)
            f.close()
            print("Done")
            return
        except:
            print ("There was some trouble. Either the path name is wrong, or an issue with the file. There has  been an issue with the file getting a \'gremlin\' in the first character. Open the file in a text editor, copy the contents, and paste into a new file. Save with the same (or similar filename) and try again.")
            return

    def do_quit(self, line):
        '''Type quiet to exit the application.'''
        return True

    def do_exit(self, line):
        '''Type exit to exit the application.'''
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    TagTerminal().cmdloop(appversion)
