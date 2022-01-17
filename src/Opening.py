# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ],  #A
                [0, 0, self.parameters['height']], #B 
                [self.parameters['width'], 0, self.parameters['height']], #C
                [self.parameters['width'], 0, 0], #D
				[0, self.parameters['thickness'], 0 ], #E 
                [0, self.parameters['thickness'], self.parameters['height']], #F 
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']], #G
                [self.parameters['width'], self.parameters['thickness'], 0], #H
                ]
        self.faces = [
                [0, 3, 2, 1], #Face ABCD
                [0, 1, 5, 4], #Face ABFE
                [4, 5, 6, 7], #Face EFGH
                [2, 3, 7, 6], #Face CDHG
                [1, 2, 6, 5], #Face BCGF
                [0, 4, 7, 3], #Face AEHD                
                ]   
        
    # Draws the faces                
    def draw(self):        
        
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face ABFE
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0,0,0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face CDHG
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], 0])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glEnd()   
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face BCGF
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glEnd()   
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face AEHD
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0,0,0])
        gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()        
    
        gl.glPopMatrix()
        
        
        
