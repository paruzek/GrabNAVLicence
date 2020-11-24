WITH object_data ([Type], [ID]) AS (
SELECT 
	CASE [Type]
            WHEN 1 THEN 'TableData'
            WHEN 2 THEN 'Form'
            WHEN 3 THEN 'Report'
            WHEN 4 THEN 'Dataport'
            WHEN 5 THEN 'Codeunit'
            WHEN 6 THEN 'XMLPort'
            WHEN 7 THEN 'MenuSuite'
            WHEN 8 THEN 'Page'
	END [Type]
	, [ID] 
	FROM  [dbo].[Object]
	WHERE   [Type] NOT IN (0,7)
)

SELECT CONCAT([Type], ',', [ID]) AS  [Object]
 FROM object_data
 ORDER BY [Type], [ID]