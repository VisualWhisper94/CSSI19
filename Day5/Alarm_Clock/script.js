// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("script is running...");

function MyAlarm (wakeup) {
    console.log ("Hey! I think you should wake up it's", wakeup);
  }
  MyAlarm ("6:30 a.m");
function momAlarm(wakeup) {
    console.log ("Hey mom!, wake up it's", wakeup);
}
momAlarm ("8:00 am")
function familyAlarm(wakeup, person){
    console.log ("Hey", person, "its", wakeup,"wake up!")

}
familyAlarm ("Karina", "9:00")
function importantAlarm(wakeup){
    return wakeup.toUpperCase ();
}
console.log (importantAlarm("wakeup!"))
function snoozeAlarm(wakeup)