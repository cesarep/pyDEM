%pythonbegin %{
import vtk
%}

%extend pyDEM::Element {
	%pythoncode %{
		def _set_vtk(self, source):
			self.mapper = vtk.vtkPolyDataMapper()
			self.mapper.SetInputConnection(source.GetOutputPort())
			self.actor = vtk.vtkActor()
			self.actor.SetMapper(self.mapper)
	%}
};

%pythonappend pyDEM::Circle::Circle(vct c, double r, Material mat, std::string group = "circles") %{
	print("_set_vtk configuração dos atores")
	print(args[1])
	self.disk = vtk.vtkRegularPolygonSource()
	self.disk.SetNumberOfSides(50)
	self.disk.SetRadius(args[1])
	self._set_vtk(self.disk)
%}

%pythonappend pyDEM::Wall::Wall(vct p1, vct p2, std::string group = "walls") %{
	lineSource = vtk.vtkLineSource()
	lineSource.SetPoint1(self.p1 + [0])
	lineSource.SetPoint2(self.p2 + [0])
	self._set_vtk(lineSource)
%}

%pythonappend pyDEM::Scene::Scene() %{
	self.ren = vtk.vtkRenderer()
	self.ren.SetBackground((.1, .2, .4))
%}

%pythonappend pyDEM::Scene::addElem(Element &elem) %{
	self.ren.AddActor(elem.actor)
%}

%extend pyDEM::Scene {
	%pythoncode %{
		def show(self):
			"""
			Renderiza a cena numa janela interativa.
			"""
			self._configRen()  
			self._startRen()        
		
		def _configRen(self):
			"""
			Configura o VTK para renderizar a cena
			"""
			# janela de rendericação
			self.renWin = vtk.vtkRenderWindow()
			self.renWin.AddRenderer(self.ren)
			self.renWin.SetSize(600, 600)
			# interação mouse-janela
			self.iren = vtk.vtkRenderWindowInteractor()
			self.iren.SetRenderWindow(self.renWin)
			# estilo de visualização de imagem 
			# scroll da zoom, e arrastar com scroll move a cena
			self.iren.SetInteractorStyle(vtk.vtkInteractorStyleImage())
			self.iren.AddObserver('ExitEvent', self.hide)
			self.iren.Initialize()
		
		def _startRen(self):
			"""
			Abre a janela de renderização
			"""
			self.renWin.Render()
			self.iren.Start()
			
		def hide(self, iren = None, event = None):
			"""
			Fecha a janela
			"""
			self.renWin.Finalize()
			self.iren.TerminateApp()
			del self.renWin, self.iren
	%}
};