using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample2USQLCSharpLib
{
    public class JsonHelper
    {
        public static string ExtractPropertiesFromJson(string jsonText)
        {
            const string sep = "|";
            JObject data = JObject.Parse(jsonText);

            StringBuilder result = new StringBuilder();
            result.Append("V161117a");
            result.Append(sep);

            try
            {
                result.Append((string)data["publisher"]);
                result.AppendFormat(sep);
            }
            catch (Exception ex)
            {
                result.AppendFormat("publisher not extracted: {0}", ex.Message);
                result.Append(sep);
            }

            try
            {
                // nb of Bytes in the first command
                result.Append(
                    System.Convert.FromBase64String(
                        (string)data["commands"][0])
                        .LongLength.ToString());
                result.AppendFormat(sep);
            }
            catch (Exception ex)
            {
                result.AppendFormat("command[0] not extracted: {0}", ex.Message);
                result.Append(sep);
            }

            return result.ToString();
        }
    }
}
