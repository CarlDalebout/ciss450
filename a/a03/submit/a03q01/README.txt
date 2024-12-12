
                                                              Named
                                                              |
                                                              Object
                                                              |
                                                              Agent               Clock  Room
                                                              |
VacuumCleanerRobotEnvironment  VacuumCleanerRobotRandomBrain  VacuumCleanerRobot
----------------------------------------------------------------------------------------------------------------------
                                                               ObjectView
                                                               |
                                                               ObjectViewText
                                                               |
EnvironmentView AgentView  AgentTextView RoomView RoomTextView ObjectTextView ObjectGUIView ClockTextView SimulatorVew
----------------------------------------------------------------------------------------------------------------------
                                                                State (base)

                                                                VacuumCleanerRobotState    ClockState    RoomState    

----------------------------------------------------------------------------------------------------------------------
Environment (base)

env.find_agents not working
----------------------------------------------------------------------------------------------------------------------
Brain
|
RandomBrain
|
SimpleBrain
----------------------------------------------------------------------------------------------------------------------
Simulator
|
DiscreteSimulator
----------------------------------------------------------------------------------------------------------------------
Problem (base)  

