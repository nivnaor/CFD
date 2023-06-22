

SELECT e.emp_id as [Employee ID], e.first_name +' '+ e.last_name as [Full Name], CONCAT(p.calling_code,'-',p.phone_number ) as [Phone Number], 
DATEDIFF(year, e.birth_date, CAST(CURRENT_TIMESTAMP as DATE)) AS Age, e.birth_date as [Date of Birth],
DATEDIFF(year, e.hire_date, CAST(CURRENT_TIMESTAMP as DATE)) AS [Years of Experience], 
case	
	when DATEDIFF(year, e.hire_date, CAST(CURRENT_TIMESTAMP as DATE)) <= 1 THEN 'Junior'
	when DATEDIFF(year, e.hire_date, CAST(CURRENT_TIMESTAMP as DATE)) <= 2 THEN 'Mid_Level'
	when DATEDIFF(year, e.hire_date, CAST(CURRENT_TIMESTAMP as DATE)) <= 6 THEN 'Intermediate'
	when DATEDIFF(year, e.hire_date, CAST(CURRENT_TIMESTAMP as DATE)) <= 10 THEN 'Senior'
end as [Experience Level],
e.hire_date as [Date of Hire],
case
	when e.company_car = 1 then 'Yes'
	else 'No'
end as [Company Car],
e.job_description as [Job Title], CONCAT('Continental ',p.city) as [Work Place],
FORMAT(e.salary,'N') as [Monthly Salary], FORMAT(e.salary * 12, 'N') as [Yearly Salary],
p.address as [Employee Address], p.postal_code as [Postal Code], p.city as City
FROM employees as e
JOIN [personal information] as p on p.[index]=e.[index]
