"""
An abstraction class for OpenGL image buffers

For simplicity, we would like to treat an image as a (1D)
list of tuples. In reality, it is a little more complicated
than that, because OpenGL expects the data in a very compact
format. This data structure abstracts all of this so we
can pretend otherwise.

You DO NOT need to understand this file (and probably will
not). This is an extremely advanced Python class. You only
need to use it.

Author: Walker M. White (wmw2)
Date:   October 20, 2017
"""
from array import array             # Byte buffers
from io import StringIO             # Making complex strings
from PIL import Image as CoreImage  # Python image processing


class Pixels(object):
    """
    A class to convert an image into a list of tuples

    The objects of the class are not lists.  But they behave
    exactly like lists in any way that matters.  It has no
    public attributes other than the buffer property, which
    allows direct access to the underlying byte buffer.

    Any initialization of this class creates an empty pixel
    list (of the requested size). Initialization of this
    list happens in other modules (to separate the logic).

    These pixels in this list are not RGB objects, like in
    Assignment 3. They are tuples, which are lists that
    cannot be modified (so you can slice them to get new
    tuples, but not assign or append to them).
    """

    @property
    def buffer(self):
        """
        The underlying byte buffer
        """
        return self._buffer

    # INITIALIZER
    def __init__(self,param):
        """
        Initializes a new pixel list

        The initializer can either create an empty pixel
        list or read one from a file, depending on the
        parameter.

        Parameter param: the creation parameter
        Precondition: param is EITHER a string with the
        name of a file OR an int >= 0
        """
        if type(param) == int:
            if param < 0:
                raise ValueError(repr(param)+' is negative')
            self._size   = param
            self._buffer = array('B',[0]*param*3)
        else:
            try:
                image = CoreImage.open(param)
                image = image.convert("RGB")
                flatten = []
                for pixel in image.getdata():
                    flatten.append(pixel[0])
                    flatten.append(pixel[1])
                    flatten.append(pixel[2])
                self._buffer = array('B',flatten)
                self._size  = image.size[0]*image.size[1]
            except:
                raise ValueError('Could not load file '+repr(param))

    # DISPLAY METHODS
    def __str__(self):
        """
        Returns: this pixel list as a string.

        The value shown will look identical to a list of
        tuples.
        """
        output = StringIO()
        output.write('[')
        after = False
        for pixel in self:
            if after:
                output.write(', ')
            output.write(str(pixel))
            after = True
        output.write(']')

        result = output.getvalue()
        output.close()

        return result

    def __repr__(self):
        """
        Returns: the unambiguous representation of this
        pixel list

        The value shown will make it clear this is a Pixels
        object and not an actual list.
        """
        return 'Pixels'+str(self)

    # LIST/SLICING METHODS
    def __len__(self):
        """
        Returns: The length of this pixel list.

        This method defines the return value of the len()
        function.
        """
        return self._size

    def __getitem__(self, index):
        """
        Returns: The element or sublist indentified by index.

        This method allows for either single element access
        (p[0]) or a slice (p[1:3]).  This method is used
        for getting elements, not setting them.

        Parameter index: The pixel list index
        Precondition: index is either an int or a slice
        """
        if type(index) == int:
            r = self._buffer[index*3  ]
            g = self._buffer[index*3+1]
            b = self._buffer[index*3+2]
            return (r,g,b)
        elif type(index) == slice:
            start = 0 if index.start is None else index.start
            stop  = self._size if index.stop is None else index.stop
            # Time to make a copy
            if index.step is None:
                result = Pixels(stop-start)
                result._buffer = self._buffer[start*3:stop*3]
            else:
                result = Pixels(len(range(start,stop,index.step)))
                opos = 0
                for npos in range(start,stop,index.step):
                    result._buffer[opos*3  ] = self._buffer[npos*3  ]
                    result._buffer[opos*3+1] = self._buffer[npos*3+1]
                    result._buffer[opos*3+2] = self._buffer[npos*3+2]
                    opos += 1
            return result
        else:
            raise TypeError('pixel indices must be integers or slices, not '+repr(type(index)))

    def __setitem__(self, index, value):
        """
        Sets the element or sublist indentified by index
        to be the new value

        This method allows for either single element access
        (p[0] = (255,0,255)) or a slice
        (p[1:3] = [(255,0,255),(0,0,0)]). This method is
        used for setting elements, not getting them.  We
        have no talked about how to set a slice in class,
        but Python supports this.

        Parameter index: The pixel list index
        Precondition: index is either an int or a slice

        Parameter value: The new value for the position or
        slice
        Precondition: index must be a tuple or a list of
        tuples
        """
        if type(index) == int:
            try:
                self._buffer[index*3  ] = value[0]
                self._buffer[index*3+1] = value[1]
                self._buffer[index*3+2] = value[2]
            except IndexError:
                raise IndexError(repr(index)+' is not a valid pixel index')
            except:
                raise ValueError(repr(value)+' is not a valid pixel')
        elif type(index) == slice:
            if not type(value) == Pixels:
                raise ValueError('attempt to assign a non-pixel sequence to a slice')
            size = len(range(index.start,index.stop,index.step))
            if len(value) == size:
                npos = 0
                for opos in range(index.start,index.stop,index.step):
                    self._buffer[opos*3  ] = value._buffer[npos*3  ]
                    self._buffer[opos*3+1] = value._buffer[npos*3+1]
                    self._buffer[opos*3+2] = value._buffer[npos*3+2]
                    npos += 1
            elif index.step is None:
                self._buffer[index.start*3:index.stop*3] = value._buffer
                self._size = len(self._buffer)//3
            else:
                raise ValueError('attempt to assign sequence of size '+str(len(value))+' to extended slice of size '+str(size))
        else:
            raise TypeError('pixel indices must be integers or slices, not '+repr(type(index)))

    def __iter__(self):
        """
        Returns: An iterator for the pixel list

        This allows the pixel list to be used in for-loops
        """
        return _PixelIterator(self)


class _PixelIterator(object):
    """
    A (hidden) class for iterating through pixel lists

    This class allows a Pixels object to be used in a
    for-loop.
    """

    def __init__(self,pixels):
        """
        Initializer: Creates an iterator for the given
        pixel list

        Paramater pixels: A pixel list
        Precondition: pixels is a Pixels object
        """
        self._pixels = pixels
        self._pos = 0
        self._len = len(pixels)

    def __next__(self):
        """
        Returns: The next element in the iteration

        This method raises StopIteration when it reaches the
        end of the iteration.  This will cause the for-loop
        to stop.
        """
        if self._pos >= self._len:
            raise StopIteration
        else:
            self._pos += 1
            return self._pixels[self._pos-1]
