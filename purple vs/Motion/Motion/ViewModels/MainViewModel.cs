using CommunityToolkit.Mvvm.ComponentModel;

namespace Motion.ViewModels;

public partial class MainViewModel : ViewModelBase
{
    [ObservableProperty]
    public partial string Greeting { get; set; } = "NIK MOK!";
}
