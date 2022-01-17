# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

from Opening import Opening

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
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
                [0, self.parameters['thickness'],self.parameters['height']], #F 
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


    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if x.parameters['thickness']==self.parameters['thickness']:
            if x.parameters['width']<self.parameters['width']:
                if x.parameters['height']<self.parameters['height']:
                    if x.parameters['position'][0]>self.parameters['position'][0] and x.parameters['position'][0]<(self.parameters['width']-x.parameters['width']):
                        if x.parameters['position'][1]==self.parameters['position'][1]:
                            if x.parameters['position'][2]>=self.parameters['position'][2] and x.parameters['position'][2]<=(self.parameters['height']-x.parameters['height']):
                                return True
        else :
            return False
                    
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
     
        Nsec=[]
        sec1=Section({'width':(x.parameters['position'][0]-self.parameters['position'][0]),'height':self.parameters['height'],'thickness':self.parameters['thickness'],'color':[42,42,42],'position':self.parameters['position'][0]})
        Nsec.append(sec1)
        sec2=Section({'width':x.parameters['width'],'height':(self.parameters['height']-x.parameters['height']),'thickness':self.parameters['thickness'],'color':[0,255,0],'position': x.parameters['height']})
        Nsec.append(sec2)
        sec3=Section({'width':(self.parameters['width']-(x.parameters['width']+x.parameters['position'][0])),'height':self.parameters['height'],'thickness':self.parameters['thickness'],'color':[0,0,255],'position':(x.parameters['width']+x.parameters['position'][0])})
        Nsec.append(sec3)
        sec4=Section({'width':x.parameters['width'],'height':x.parameters['position'][2],'thickness':self.parameters['thickness'],'color':[123,123,132],'position':x.parameters['position'][0]})        
        Nsec.append(sec4)
        return Nsec
    
    
    
    
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arrêtes de ABCD
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        gl.glVertex3fv([0,0,0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()
            
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arrêtes ABFE
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        gl.glVertex3fv([0,0,0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
        gl.glEnd()
            
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arrêtes EFGH
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()   
            
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arrêtes CDHG
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], 0])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glEnd()   
            
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arrêtes BCGF
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glEnd()   
            
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arrêtes AEHD
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        gl.glVertex3fv([0,0,0])
        gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()
                    
    # Draws the faces
    def draw(self):
            gl.glPushMatrix()        
            if self.parameters['edges'] == True :
                self.drawEdges()
        # A compléter en remplaçant pass par votre code
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face ABCD
            
            #gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
            
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
            gl.glVertex3fv([0,0,0])
            gl.glVertex3fv([0, 0, self.parameters['height']])
            gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
            gl.glVertex3fv([self.parameters['width'], 0, 0])
            gl.glEnd()
            
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face ABFE
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
            gl.glVertex3fv([0,0,0])
            gl.glVertex3fv([0, 0, self.parameters['height']])
            gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
            gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
            gl.glEnd()
            
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace la face EFGH
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
            gl.glVertex3fv([0, self.parameters['thickness'], 0 ])
            gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
            gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
            gl.glVertex3fv([self.parameters['width'], 0, 0])
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
