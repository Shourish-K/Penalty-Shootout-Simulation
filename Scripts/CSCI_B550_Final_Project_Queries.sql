-- Selecting TOP 10 Players with the Highest Shot Accuracy

SELECT TOP 10 [Index], Position, Name
FROM ShotTakers
ORDER BY SHO DESC

-- Selecting TOP 10 Players with the Lowest Shot Accuracy

SELECT TOP 10 [Index], Position, Name
FROM ShotTakers
ORDER BY SHO

-- Select Goalkeeper with Highest Shot Accuracy

SELECT TOP 1 [Index], Position, Name
FROM Goalkeepers
ORDER BY SHO DESC

-- Select Goalkeeper with Lowest Shot Accuracy

SELECT TOP 1 [Index], Position, Name
FROM Goalkeepers
ORDER BY SHO

-- Select Man Utd team with descending order of OVR

SELECT TOP 10 [Index], Position, Name
FROM ShotTakers
WHERE Team = 'Man Utd'
ORDER BY OVR DESC

-- Select Man Utd team with descending order of Penalties

SELECT TOP 10 [Index], Position, Name
FROM ShotTakers
WHERE Team = 'Man Utd'
ORDER BY Penalties DESC
