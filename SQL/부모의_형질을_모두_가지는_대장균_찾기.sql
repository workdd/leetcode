select C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
from ECOLI_DATA C
JOIN ECOLI_DATA P
ON C.PARENT_ID = P.ID
WHERE (C.GENOTYPE & P.GENOTYPE) = P.GENOTYPE
ORDER BY C.ID;