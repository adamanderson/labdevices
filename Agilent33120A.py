import serial

class Agilent33120A:
    def __init__(self, port='/dev/ttyr10',
                 baudrate=9600,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_TWO,
                 bytesize=serial.EIGHTBITS):
        self.interface = serial.Serial(port, baudrate,
                                       parity=parity,
                                       stopbits=stopbits,
                                       bytesize=bytesize)
        self.term_string = b'\r\n'

        
    def set_shape(self, shape):
        '''
        Parameters
        ----------
        shape : str
            String indicating function shape to set. Must be one of:
            'SIN', 'SQU', 'TRI', 'RAMP', 'NOIS', 'DC', 'USER'

        Returns
        -------
        None
        '''
        if shape in [b'SIN', b'SQU', b'TRI', b'RAMP', b'NOIS', b'DC', b'USER']:
            self.interface.write(b'FUNC:SHAP %s %s' % (shape,
                                                       self.term_string))
        else:
            print('Invalid shape. Doing nothing.')
            
    
    def set_frequency(self, frequency):
        '''
        Parameters
        ----------
        frequency : float
            Frequency of waveform to set.

        Returns
        -------
        None
        '''
        self.interface.write(b'FREQ %f %s' % (frequency,
                                              self.term_string))

    def set_amplitude(self, amplitude):
        '''
        Parameters
        ----------
        frequency : float
            Frequency of waveform to set.

        Returns
        -------
        None
        '''
        self.interface.write(b'VOLT %.3f %s' % (amplitude,
                                                self.term_string))
        print(b'VOLT %.3f %s' % (amplitude, self.term_string))
