using BlazorServer.Services;
using EmployeeManagement.Models;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorServer.Pages
{
    public class DepartmentListBase : ComponentBase
    {
        [Inject]
        public IDepartmentService DepartmentService { get; set; }
        public IEnumerable<Department> Departments { get; set; }
        protected override async Task OnInitializedAsync()
        {
            Departments = (await DepartmentService.GetDepartments()).ToList();
        }
    }
}
