

class menu():
    def __init__(self, MenuChoices, NewGame, GameType, StartGame, SaveGame, Exit, CurrentSelection):
        ''' Beginning menu state '''
        
        self.MenuChoices = MenuChoices
        
        self.NewGame = NewGame
        self.GameType = GameType
        
        self.StartGame = StartGame
        self.SaveGame= SaveGame
        self.Exit = Exit
        
        self.CurrentSelection = CurrentSelection
        
        self.MenuChoices = {} 
        ''' How? '''
        
        return 
    
    
    ''' MAIN CHOICES '''
    
    def OnPressPlay(self):
        return
    
    def OnPressLoad(self):
        return
    
    def OnPressTutorial(self):
        return
    
    def OnPressSettings(self):
        return
    
    def OnPressExit(self):
        return
    
    ''' END OF MAIN MENU CHOICES '''
    
    ''' ALSO PAUSE GAME MENU CHOICES '''
    
    def OnPressPauseGame(self):
        return
    
    def OnPressSaveGame(self):
        return
    
    def OnPressExitAfterPressPauseGame(self):
        return
    
    ''' END OF PAUSE GAME MENU CHOICES '''
    
    
    def OnStartingCharacterSelection(self):
        return
        
    def OnMenuSelection(self):
        return
    
    def OnNewGame(self):
        return 
    
    def OnStartGame(self):
        return 
    
    def OnSaveGame(self):
        return
    
    def OnBuild(self):
        return 
    
    def OnExit(self):
        return 
    
    def Update(self):
        return 
        
    def Run(self):
        self.Update()
        
        
