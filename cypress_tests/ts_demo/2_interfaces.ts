interface IProject {
  readonly project_id: number;
  project_name: string;
  created_at: any;
  user: string;
  created_by?: string;
  project_content: {
    stills: number;
    vt_tours: number;
  };
}

const project_1: IProject = {
  project_id: 1,
  project_name: "First Project",
  created_at: new Date(),
  user: "Mihluha Maklay",
  project_content: {
    stills: 10,
    vt_tours: 5,
  },
};
const project_2 = {} as IProject;
const project_3 = <IProject>{};

interface IProjectWithUser extends IProject {
  getUser: () => number;
}

const project_4: IProjectWithUser = {
  project_id: 1,
  project_name: "First Project",
  created_at: new Date(),
  user: "Mikluha Maklay",
  project_content: {
    stills: 10,
    vt_tours: 5,
  },
  getUser(): number {
    return this.user;
  },
};

console.log(project_4.getUser());

interface IClock {
  time: Date;
  setTime(date: Date): void;
}

class Clock implements IClock {
  time: Date = new Date();
  setTime(date: Date): void {
    this.time = date;
  }
}

interface IStyles {
  [key: string]: string;
}

const css: IStyles = {
  border: "1px solid black",
  marginTop: "2px",
  borderRadius: "5px",
};
